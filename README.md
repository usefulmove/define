# define

A small command-line dictionary. Look up English word definitions straight from the terminal, with colorized output.

It queries the free [Free Dictionary API](https://dictionaryapi.dev/) and prints each part of speech with its numbered definitions.

## Requirements

- Python >= 3.13

## Installation

### With `pipx` from GitHub

Install directly from the GitHub repository without cloning:

```bash
pipx install git+https://github.com/usefulmove/define.git
```

This builds the package, exposes the `define` command on your `PATH`, and lets you run it from anywhere:

```bash
define hello
```

To upgrade after a new release:

```bash
pipx upgrade define
```

To uninstall:

```bash
pipx uninstall define
```

### With `uv` for local development

Install it as a global CLI tool from the project directory:

```bash
uv tool install .
```

This builds the package, exposes the `define` command on your `PATH`, and lets you run it from anywhere:

```bash
define hello
```

If `uv` warns that its tool bin directory is not on your `PATH`, add it (uv prints the path — commonly `~/.local/bin`).

To upgrade after changing the code:

```bash
uv tool install . --force
```

To uninstall:

```bash
uv tool uninstall define
```

### With `uv run` (no install)

Run it directly from the project directory without installing anything:

```bash
uv run define hello
```

### With `pip`

```bash
pip install .
define hello
```

## Usage

```bash
define <word>
```

Examples:

```bash
define hello
define serendipity
```

Output shows the word, each part of speech, and numbered definitions, e.g.:

```
hello
  noun:
    1. "Hello!" or an equivalent greeting.
  ...
```

## Notes

- Requires an internet connection; the tool fetches definitions live from `https://api.dictionaryapi.dev`.
