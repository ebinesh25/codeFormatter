# Code Formatter

This project provides a set of tools for formatting code in various programming languages, including Python, JavaScript, C, C++, Java, PHP, and SQL. It includes a Docker setup for easy installation and usage of the formatters.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Supported Languages](#supported-languages)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install the necessary dependencies, you can either use the provided Dockerfile or run the installation script directly on your system.

### Using Docker

1. Build the Docker image:

   ```bash
   docker build -t code-formatter .
   ```

2. Run the Docker container:

   ```bash
   docker run -it --rm -v $(pwd):/workspace code-formatter
   ```

### Using the Installation Script

Alternatively, you can run the installation script directly on your system:

```bash
bash codeFormatter/installDependencies.sh
```


This script will install the following dependencies:

- Python and pip
- Black (Python formatter)
- Node.js and npm
- Prettier (JavaScript, HTML, CSS, and JSON formatter)
- Clang-format (C, C++, and Java formatter)
- PHP and PHP-CS-Fixer
- SQL Formatter CLI

## Usage

To format your code, you can use the `format_code` function from the `formatCode.py` module. Here’s an example of how to use it:

```python
from formatCode import format_code

code = "your unformatted code here"
language = "python" # specify the language

formatted_code = format_code(code, language)

print(formatted_code)
```

## Supported Languages

The following programming languages are supported:

- Python
- JavaScript
- HTML
- CSS
- JSON
- C
- C++
- Java
- PHP
- SQL

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.