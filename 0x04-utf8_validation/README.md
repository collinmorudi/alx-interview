# 0x04. UTF-8 Validation

## Project Overview
This project focuses on validating UTF-8 encoded data using Python. UTF-8 encoding is a variable-width character encoding, allowing each character to be represented by 1 to 4 bytes. A valid UTF-8 encoding follows specific rules that this project will help verify.

The key objective is to determine whether a given list of integers represents a valid UTF-8 encoded sequence by utilizing Python's bitwise operations.

## Requirements
- **Python Version**: Python 3.4.3
- **Operating System**: Ubuntu 20.04 LTS
- **Editor**: vi, vim, emacs
- **PEP 8 Style Compliance**: Version 1.7.x
- **Executable Files**: All Python files must be executable
- **Mandatory File**: `README.md` in the root directory

## Task
### 0. UTF-8 Validation
Write a method `validUTF8(data)` that determines if a list of integers represents a valid UTF-8 encoding.

#### Prototype
```python
def validUTF8(data):
