# Regex Simplification Tool

This tool leverages Claude 3.7 Sonnet to simplify complex regular expressions while preserving their matching behavior. It validates the simplifications using the ABC automata-based regex comparison tool.

## Features

- Simplify complex regular expressions using Claude 3.7 Sonnet
- Validate simplifications using ABC automata comparison
- Calculate reduction in regex length and Jaccard similarity
- Support for thinking mode (showing Claude's reasoning)
- Generate detailed reports of simplification results
- Process individual or batches of regex patterns

## Prerequisites

- Python 3.6+
- Anthropic API key
- ABC tool installed

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install anthropic
   ```
3. Set up your Anthropic API key:
   ```
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

### Basic Usage

```
python anthropic_regex_processor.py
```

### Command-Line Options

| Option | Description |
|--------|-------------|
| `--no-thinking` | Disable thinking mode (use standard mode without showing reasoning) |
| `--markdown-file FILE` | Path to markdown file containing regex patterns (default: "Regex Dataset.md") |
| `--start-index N` | Index to start processing from (1-based, default: 1) |

### Examples

Process all regexes with thinking mode:
```
python anthropic_regex_processor.py
```

Process regexes without thinking mode:
```
python anthropic_regex_processor.py --no-thinking
```

Use a custom markdown file:
```
python anthropic_regex_processor.py --markdown-file my_regexes.md
```

Start from a specific regex:
```
python anthropic_regex_processor.py --start-index 5
```

## Input Format

The default input file (`Regex Dataset.md`) should follow this format:

```
1. **Description of regex** 
```regex_pattern```

2. **Another description** 
```another_regex_pattern```
```

## Output Files

The tool generates two report files:

1. `regex_simplification_report.md`: Basic report with original regex, simplified regex, and statistics
2. `regex_simplification_detailed_report.md`: Enhanced report including Claude's thinking process

## ABC Validation

The tool uses ABC to validate that the simplified regex matches exactly the same strings as the original. The validation calculates:

- Jaccard Index Numerator: Measure of intersection between original and simplified regex
- Jaccard Index Denominator: Measure of union between original and simplified regex
- Jaccard Similarity: Ratio of numerator to denominator (values closer to 1.0 indicate higher similarity)

## Interactive Mode

During processing, the tool allows you to:
- Continue to the next regex by typing `next`
- Jump to a specific regex by typing `jump N` (where N is the index)
- Exit the program by typing `exit`

## Troubleshooting

### API Key Issues

If you encounter API key issues:
```
Error: ANTHROPIC_API_KEY environment variable not set.
```
Make sure you've properly set your Anthropic API key as an environment variable.

### ABC Tool Not Found

If ABC tool validation fails:
```
Error running ABC: [Errno 2] No such file or directory
```
Ensure the ABC tool path is correctly specified in the script.

### Proxy Issues

If you're behind a proxy, the script attempts to handle proxy settings automatically. If you encounter connection issues, check your proxy configuration.

## File Structure

- `anthropic_regex_processor.py`: Main script
- `Regex Dataset.md`: Input file containing regex patterns
- `regex_simplification_report.md`: Output report
- `regex_simplification_detailed_report.md`: Detailed output report with thinking
- `complex_regex.txt`: Temporary file for original regex
- `simple_regex.txt`: Temporary file for simplified regex
- `dummy.smt2`: Required dummy file for ABC

## Contributors

This tool was developed as part of the "Verifying LLM Generated Policies" project. 