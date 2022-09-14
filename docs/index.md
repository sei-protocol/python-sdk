# For Developers

## Installation

First, [install Poetry](https://python-poetry.org/docs/#installation):

=== "Linux/macOS"

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

=== "Windows"

    ```powershell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```

Then install the dev environment:

```bash
poetry install
```

Activate the virtual environment created automatically by Poetry:

```bash
poetry shell
```

To install/remove a dependency

```bash
poetry add/remove <library_name>
```

## Packaging and Distribution

```bash
$ poetry build
```

This will generate `dist/app-1.0.0.tar.gz` and `dist/app-1.0.0-py3-none-any.whl`.

Then

```bash
$ poetry publish
```

## Enture Code Quality with nox

Run all checks locally

```bash
(python-sdk-py3.10) $ nox
```

Run unit tests

```bash
(python-sdk-py3.10) $ nox -s test
```

Lint checks

```bash
(python-sdk-py3.10) $ nox -s lint
```

Code formatter

```bash
(python-sdk-py3.10) $ nox -s fmt
```

Type check

```bash
(python-sdk-py3.10) $ nox -s type_check
```

Generate Markdown docs

```bash
(python-sdk-py3.10) $ nox -s docs
```
