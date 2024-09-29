# Pythia Suggest

Pythia Suggest is a tool designed to automatically generate docstrings for Python files using the power of large language models (LLMs). By analyzing your Python code, Pythia Suggest creates detailed and accurate documentation for functions and classes, making your code more understandable and maintainable.

## Features

- **Automatic Docstring Generation**: Pythia Suggest scans your Python files and generates informative docstrings for functions and classes.
- **Large Language Model Integration**: Leverages state-of-the-art LLMs to create high-quality, human-readable docstrings.
- **Customizable**: You can configure docstring formats to match your preferred style.
- **Easy to Use**: Simple command-line interface (CLI) to generate docstrings for your entire project or specific files.

## Installation

To install Pythia Suggest, you can use `pip`:

```bash
pip install pythia-suggest
```

## Usage

After installing, you can generate docstrings for a Python file or an entire directory with the following commands:

```bash
# Generate docstrings for a specific Python file
pythia-suggest generate myfile.py

# Generate docstrings for all Python files in a directory
pythia-suggest generate ./myproject/
```

### Command-line Options

- `--overwrite`: Overwrite existing docstrings in your files.
- `--style`: Specify the docstring style (e.g., Google, NumPy, or reStructuredText).

## Example

Before running Pythia Suggest:

```python
def add_numbers(a, b):
    return a + b
```

After running Pythia Suggest:

```python
def add_numbers(a, b):
    """
    Adds two numbers together.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b
```

## Contributing

We welcome contributions! If you'd like to improve Pythia Suggest, please fork the repository and submit a pull request.

## License

Pythia Suggest is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
