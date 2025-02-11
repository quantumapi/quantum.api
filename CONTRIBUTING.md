# Contributing to Quantum.API

We welcome contributions from the community! Whether you're fixing a bug, adding a new feature, or improving documentation, your help is greatly appreciated. Please take a moment to review this guide before contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)

## Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [contact@example.com](mailto:contact@example.com).

## How to Contribute

### Reporting Bugs

1. **Search for existing issues**: Before creating a new issue, please search the [issue tracker](https://github.com/quantumapi/quantum.api/issues) to see if the issue has already been reported.
2. **Create a new issue**: If your issue is not already reported, create a new issue with a descriptive title and detailed description. Include steps to reproduce the issue, expected behavior, and actual behavior.

### Suggesting Enhancements

1. **Search for existing issues**: Before creating a new issue, please search the [issue tracker](https://github.com/quantumapi/quantum.api/issues) to see if the enhancement has already been suggested.
2. **Create a new issue**: If your enhancement is not already suggested, create a new issue with a descriptive title and detailed description. Explain the use case and benefits of the enhancement.

### Pull Requests

1. **Fork the repository**: Fork the repository to your own GitHub account.
2. **Create a new branch**: Create a new branch for your changes.
3. **Make your changes**: Implement your changes and ensure that all tests pass.
4. **Update documentation**: If your changes affect the API or user interface, update the documentation accordingly.
5. **Create a pull request**: Create a pull request with a descriptive title and detailed description. Reference any related issues.

## Development Setup

1. **Clone the repository**:

```bash
git clone https://github.com/quantumapi/quantum.api.git
cd quantum.api
```

2. **Set up a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**:

Create a `.env` file based on `.env.example` and fill in the necessary values.

5. **Run the application**:

```bash
uvicorn main:app --reload
```

## Coding Standards

- Follow PEP 8 for Python code style.
- Write clear and concise comments.
- Include docstrings for all public modules, classes, and functions.
- Write unit tests for all new features and bug fixes.
- Ensure all tests pass before submitting a pull request.

Thank you for your contributions!
