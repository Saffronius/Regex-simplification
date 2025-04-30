#!/usr/bin/env python3
import subprocess

def run_comparison():
    """
    Run the ABC command to compare the two regex files.
    """
    cmd = [
        "/home/ash/Desktop/VerifyingLLMGeneratedPolicies/ABC/src/abc",
        "-i", "dummy.smt2",
        "--compare-regexes", "complex_regex.txt", "simple_regex.txt",
        "-bs", "100"
    ]
    
    print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, check=True, text=True)
        print("Command completed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    run_comparison() 