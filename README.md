# uv-template

A Python project template using `uv` package manager.

## Features

- Modern Python package structure using `src` layout
- Package management with `uv`
- Development tools:
  - Testing with `pytest`
  - Code formatting with `ruff`
  - Type checking with `mypy`
  - Documentation with `mkdocs` and `mkdocs-material`
  - Pre-commit hooks
  - Continuous Integration with `tox`

## Usage

This project uses a Makefile to provide convenient commands for development tasks:

```bash
# Install virtual environment and pre-commit hooks
make install

# Run code quality tools (linting, type checking, etc.)
make check

# Run tests with pytest
make test

# Build documentation
make docs

# Build the package
make build

# Build and publish to PyPI
make build-and-publish

# Show all available commands
make help
```

## Documentation

Detailed documentation is available at [https://entelecheia.github.io/uv-template/](https://entelecheia.github.io/uv-template/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
