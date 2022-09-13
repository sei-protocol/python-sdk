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

Then install the `fact` package and its dependencies:

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

This will generate `dist/fact-1.0.0.tar.gz` and `dist/fact-1.0.0-py3-none-any.whl`.

Then

```bash
$ poetry publish
```

## Enture Code Quality with nox

Run all checks locally

```bash
(fact) $ nox
```

Run unit tests

```bash
(fact) $ nox -s test
```

Lint checks

```bash
(fact) $ nox -s lint
```

Code formatter

```bash
(fact) $ nox -s fmt
```

Type check

```bash
(fact) $ nox -s type_check
```

Generate Markdown docs

```bash
(fact) $ nox -s docs
```
