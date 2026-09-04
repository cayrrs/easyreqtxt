# easyreqtxt

A Python command-line tool that creates `requirements.txt` files by scanning a Python project for its imports.

## Installation

Clone the repository:

```bash
git clone https://github.com/cayrrs/easyreqtxt.git
cd easyreqtxt
```

Install easyreqtxt:

```bash
pip install -e .
```

## Usage

Provide the directory you want to scan:

```bash
easyreqtxt <folder>
```

For example:

```bash
easyreqtxt .
```

This recursively scans the directory for Python files and creates a `requirements.txt` file.

### Custom Output File

Use `-o` or `--output` to specify a different output file:

```bash
easyreqtxt . -o requirements-dev.txt
```

## How It Works

easyreqtxt:

1. Recursively finds Python files in the specified directory.
2. Finds imported modules using Python's AST parser.
3. Ignores Python standard-library modules.
4. Resolves imported modules to installed packages.
5. Retrieves the installed package versions.
6. Writes the dependencies to the output file.

For example, a project containing:

```python
import requests
import numpy
import json
```

could produce:

```text
requests==2.32.5
numpy==2.3.3
```

The `json` module is excluded because it is part of Python's standard library.

## Requirements

Python 3.14 or newer.

## License

This project is licensed under the Unlicense (do whatever you want) License. See the [LICENSE](LICENSE) file for details.