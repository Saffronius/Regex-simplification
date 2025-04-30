#!/usr/bin/env python3
import re
import subprocess
import os
import sys
import time
import anthropic
import argparse
from pathlib import Path

def extract_regexes_from_markdown(markdown_file):
    """Extract regex patterns from the markdown file."""
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract numbered items and their regex patterns
    regexes = []
    regex_names = []
    
    # Split by numbered items
    pattern = r'(\d+)\.\s+\*\*([^*]+)\*\*\s+```\s*(.*?)\s*```'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for match in matches:
        item_num, name, regex = match
        regexes.append(regex.strip())
        regex_names.append(f"{item_num}. {name.strip()}")
    
    return regexes, regex_names

def save_regex_to_file(regex, filename):
    """Save a regex pattern to a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(regex)
    print(f"Saved regex to {filename} ({len(regex)} characters)")

def analyze_abc_output(output):
    """Extract Jaccard index data from ABC output."""
    lines = output.split('\n')
    numerator = "Not found"
    denominator = "Not found"
    
    for line in lines:
        if "jaccard index numerator" in line:
            numerator = line.split(":")[-1].strip()
        elif "jaccard index denominator" in line:
            denominator = line.split(":")[-1].strip()
    
    return numerator, denominator

def validate_with_abc(complex_file, simple_file):
    """Run ABC to compare the regexes."""
    cmd = [
        "/home/ash/Desktop/VerifyingLLMGeneratedPolicies/ABC/src/abc",
        "-i", "dummy.smt2",
        "--compare-regexes", complex_file, simple_file,
        "-bs", "100"
    ]
    
    print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout + "\n" + result.stderr
        return result.returncode == 0, output
    except Exception as e:
        print(f"Error running ABC: {e}")
        return False, str(e)

def simplify_regex_with_claude(regex, regex_name="", use_thinking=True):
    """Use Anthropic API to simplify the regex with Claude 3.7 Sonnet."""
    try:
        # Check for API key
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            print("Error: ANTHROPIC_API_KEY environment variable not set.")
            print("Please set it with: export ANTHROPIC_API_KEY=your_api_key")
            return None, None
        
        # Create client - without proxies
        # Remove any proxy settings from environment variables temporarily
        http_proxy = os.environ.pop('HTTP_PROXY', None)
        https_proxy = os.environ.pop('HTTPS_PROXY', None)
        
        try:
            client = anthropic.Anthropic(api_key=api_key)
        finally:
            # Restore proxy settings
            if http_proxy:
                os.environ['HTTP_PROXY'] = http_proxy
            if https_proxy:
                os.environ['HTTPS_PROXY'] = https_proxy
        
        # Add context about what the regex matches
        context = ""
        if regex_name:
            context = f"This regex is designed to match {regex_name}."
        
        # Prepare prompt
        prompt = f"""Simplify this regular expression without changing what strings it matches:

{context}

Regular expression to simplify:
```
{regex}
```

Provide ONLY the simplified regex pattern in your answer, with no additional text or explanation."""
        
        # Create message parameters
        message_params = {
            "model": "claude-3-7-sonnet-20250219",
            "max_tokens": 8000,
            "temperature": 1,
            "system": """You are a regex simplification expert. Your task is to analyze regular expressions and create simplified versions that match EXACTLY the same set of strings as the original - not a single string different. 

Key requirements:
1. The simplified regex must match EXACTLY the same language as the original
2. Prioritize making the regex shorter and more readable
3. Remove redundant groups, unnecessary escapes, and simplify character classes
4. Preserve all boundary conditions and edge cases
5. AVOID CHANGING THE UNDERLYING MATCHING BEHAVIOR AT ALL COSTS

Your simplifications will be verified by comparing the automata of both expressions.""",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
        }
        
        # Add thinking parameters if enabled
        if use_thinking:
            message_params["thinking"] = {
                "type": "enabled",
                "budget_tokens": 4000
            }
            print("Using thinking mode with budget of 4000 tokens")
        else:
            print("Using standard mode without thinking")
        
        # Call Claude 3.7 Sonnet
        message = client.messages.create(**message_params)
        
        # Extract the response - properly handle different content types
        simplified_regex = None
        thinking_block = None
        
        # Print response structure for debugging
        print("Response structure:", type(message.content))
        
        # Iterate through content items and look for actual text content and thinking
        for content_item in message.content:
            # Find thinking block if present
            if hasattr(content_item, 'type') and content_item.type == 'thinking' and hasattr(content_item, 'thinking'):
                thinking_block = content_item.thinking
                continue
                
            # Find text content
            if hasattr(content_item, 'text'):
                text = content_item.text.strip()
                if text:
                    simplified_regex = text
                    break
        
        if not simplified_regex:
            print("Could not find simplified regex in Claude's response.")
            if message.content:
                print("Available content:")
                for i, content_item in enumerate(message.content):
                    print(f"Item {i}: Type: {type(content_item)}")
                    if hasattr(content_item, 'type'):
                        print(f"  Content type: {content_item.type}")
            return None, None
        
        # Remove any markdown formatting if present
        if simplified_regex.startswith("```") and simplified_regex.endswith("```"):
            # Extract content between backticks
            lines = simplified_regex.split('\n')
            # If it's a code block with language marker
            if len(lines) > 2:
                simplified_regex = '\n'.join(lines[1:-1])
            else:
                simplified_regex = simplified_regex[3:-3].strip()
        
        return simplified_regex, thinking_block
    
    except Exception as e:
        print(f"Error calling Anthropic API: {e}")
        print("Exception details:", type(e).__name__)
        import traceback
        traceback.print_exc()
        return None, None

def process_regex(regex, name, index, report_file, detailed_report_file, use_thinking=True):
    """Process a single regex, simplify it and validate."""
    print(f"\n{'='*80}")
    print(f"Processing regex {index+1}: {name}")
    print(f"{'='*80}")
    
    # Save the complex regex
    save_regex_to_file(regex, "complex_regex.txt")
    
    # Display the current regex
    print(f"Original regex ({len(regex)} chars):")
    print("-" * 40)
    print(regex)
    print("-" * 40)
    
    # Use Claude to simplify the regex
    print("\nSending to Claude 3.7 Sonnet for simplification...")
    simplified, thinking_block = simplify_regex_with_claude(regex, name, use_thinking)
    
    if not simplified:
        print("Failed to get simplified regex from Claude. Skipping this regex.")
        return False
    
    print(f"\nSimplified regex ({len(simplified)} chars):")
    print("-" * 40)
    print(simplified)
    print("-" * 40)
    
    # Save the simplified regex
    save_regex_to_file(simplified, "simple_regex.txt")
    
    # Validate with ABC
    success, output = validate_with_abc("complex_regex.txt", "simple_regex.txt")
    
    # Display the ABC output
    print("\nABC Output:")
    print("-" * 40)
    print(output)
    print("-" * 40)
    
    # Extract Jaccard index data
    numerator, denominator = analyze_abc_output(output)
    
    # Calculate Jaccard similarity
    jaccard_similarity = "N/A"
    try:
        num = float(numerator)
        den = float(denominator)
        if den > 0:  # Avoid division by zero
            jaccard_similarity = f"{(num / den):.4f}"
    except (ValueError, TypeError):
        # If the values couldn't be converted to float
        pass
    
    # Calculate reduction percentage
    original_len = len(regex)
    simplified_len = len(simplified)
    reduction = ((original_len - simplified_len) / original_len) * 100 if original_len > 0 else 0
    
    # Create statistics for both reports
    statistics = [
        f"- Reduction: {reduction:.2f}%",
        f"- ABC Validation: {'Success' if success else 'Failed'}",
        f"- Jaccard Index Numerator: {numerator}",
        f"- Jaccard Index Denominator: {denominator}",
        f"- Jaccard Similarity: {jaccard_similarity}"
    ]
    
    # Append to regular report
    with open(report_file, 'a', encoding='utf-8') as f:
        f.write(f"\n## Regex {index+1}: {name}\n\n")
        f.write(f"### Original ({original_len} chars)\n")
        f.write(f"```\n{regex}\n```\n\n")
        f.write(f"### Simplified ({simplified_len} chars)\n")
        f.write(f"```\n{simplified}\n```\n\n")
        f.write(f"### Statistics\n")
        f.write("\n".join(statistics))
        f.write("\n\n" + "-"*80 + "\n")
    
    # Append to detailed report (including thinking block)
    with open(detailed_report_file, 'a', encoding='utf-8') as f:
        f.write(f"\n## Regex {index+1}: {name}\n\n")
        f.write(f"### Original ({original_len} chars)\n")
        f.write(f"```\n{regex}\n```\n\n")
        f.write(f"### Simplified ({simplified_len} chars)\n")
        f.write(f"```\n{simplified}\n```\n\n")
        f.write(f"### Statistics\n")
        f.write("\n".join(statistics))
        f.write("\n\n")
        
        if thinking_block:
            f.write(f"### Thinking Process\n")
            f.write("```\n")
            f.write(thinking_block)
            f.write("\n```\n\n")
        else:
            f.write(f"### Thinking Process\n")
            f.write("No thinking process available (using standard mode or thinking not returned).\n\n")
            
        f.write("-"*80 + "\n")
    
    print(f"\nCompleted processing regex {index+1}")
    print(f"Validation {'successful' if success else 'failed'}")
    print(f"Reduction: {reduction:.2f}%")
    print(f"Jaccard Similarity: {jaccard_similarity}")
    
    return success

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Process and simplify regular expressions using Claude 3.7 Sonnet")
    parser.add_argument("--no-thinking", action="store_true", help="Disable thinking mode (use standard mode)")
    parser.add_argument("--markdown-file", default="Regex Dataset.md", help="Path to markdown file with regexes")
    parser.add_argument("--start-index", type=int, default=1, help="Index to start processing from (1-based)")
    args = parser.parse_args()
    
    # Setup file paths
    markdown_file = args.markdown_file
    report_file = "regex_simplification_report.md"
    detailed_report_file = "regex_simplification_detailed_report.md"
    
    # Use thinking mode unless --no-thinking was specified
    use_thinking = not args.no_thinking
    mode_str = "standard mode" if not use_thinking else "thinking mode"
    
    # Initialize report files
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    
    # Regular report
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Regex Simplification Report\n\n")
        f.write(f"This report contains the results of simplifying complex regular expressions using Claude 3.7 Sonnet ({mode_str}).\n\n")
        f.write(f"Generated on: {timestamp}\n\n")
        f.write("-"*80 + "\n")
    
    # Detailed report with thinking
    with open(detailed_report_file, 'w', encoding='utf-8') as f:
        f.write("# Regex Simplification Detailed Report\n\n")
        f.write(f"This report contains the results of simplifying complex regular expressions using Claude 3.7 Sonnet ({mode_str}), including thinking processes.\n\n")
        f.write(f"Generated on: {timestamp}\n\n")
        f.write("-"*80 + "\n")
    
    # Check if markdown file exists
    if not os.path.exists(markdown_file):
        print(f"Error: Markdown file '{markdown_file}' not found.")
        return 1
    
    # Check if dummy.smt2 exists
    if not os.path.exists("dummy.smt2"):
        print("Error: dummy.smt2 file not found.")
        return 1
    
    # Check for Anthropic API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable not set.")
        print("Please set it with: export ANTHROPIC_API_KEY=your_api_key")
        return 1
    
    # Extract regexes
    regexes, names = extract_regexes_from_markdown(markdown_file)
    
    if not regexes:
        print("No regexes found in the markdown file.")
        return 1
    
    print(f"Found {len(regexes)} regexes in {markdown_file}")
    print(f"Using Claude 3.7 Sonnet in {mode_str}")
    
    # Get starting index from command line or prompt if not provided
    start_index = args.start_index - 1  # Convert to 0-based index
    if start_index < 0:
        start_index = 0
    if start_index >= len(regexes):
        start_index = len(regexes) - 1
    
    print(f"Starting from regex #{start_index + 1}")
    
    # Process each regex
    success_count = 0
    processed_count = 0
    i = start_index
    while i < len(regexes):
        regex = regexes[i]
        name = names[i] if i < len(names) else f"Regex {i+1}"
        
        # Skip empty regexes
        if not regex.strip():
            i += 1
            continue
        
        try:
            processed_count += 1
            if process_regex(regex, name, i, report_file, detailed_report_file, use_thinking):
                success_count += 1
                
            # If the simplification failed, try again with a modified prompt
            # This code could be added here if needed
            
        except Exception as e:
            print(f"Error processing regex {i+1}: {e}")
            with open(report_file, 'a', encoding='utf-8') as f:
                f.write(f"\n## Regex {i+1}: {name}\n\n")
                f.write(f"Error: {str(e)}\n")
                f.write("\n" + "-"*80 + "\n")
            
            with open(detailed_report_file, 'a', encoding='utf-8') as f:
                f.write(f"\n## Regex {i+1}: {name}\n\n")
                f.write(f"Error: {str(e)}\n")
                f.write("\n" + "-"*80 + "\n")
        
        # Ask if we should continue or exit
        print("\nEnter 'next' to continue to the next regex, 'exit' to stop, or 'jump N' to jump to regex N:")
        choice = input("> ").strip().lower()
        
        if choice == 'exit':
            break
        elif choice.startswith('jump '):
            try:
                jump_to = int(choice.split()[1]) - 1
                if 0 <= jump_to < len(regexes):
                    i = jump_to - 1  # Subtract 1 because we'll add 1 below
            except:
                pass
        
        i += 1
    
    # Final report summary for both reports
    summary = [
        "\n# Summary\n\n",
        f"- Regexes processed: {processed_count} of {len(regexes)}\n",
        f"- Successfully validated: {success_count}\n",
        f"- Failed validation: {processed_count - success_count}\n",
        f"- Using Claude 3.7 Sonnet in {mode_str}\n"
    ]
    
    with open(report_file, 'a', encoding='utf-8') as f:
        f.write("\n".join(summary))
    
    with open(detailed_report_file, 'a', encoding='utf-8') as f:
        f.write("\n".join(summary))
    
    print(f"\nSummary:")
    print(f"- Regexes processed: {processed_count} of {len(regexes)}")
    print(f"- Successfully validated: {success_count}")
    print(f"- Failed validation: {processed_count - success_count}")
    print(f"Report saved to {report_file}")
    print(f"Detailed report with thinking saved to {detailed_report_file}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 