# vban-cli

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

---

## Install

#### With uv

```console
uv tool install vban-cli
```

#### With pipx

```console
pipx install vban-cli
```

The CLI should now be discoverable as `vban-cli`

---

## Configuration

### Flags

```console
vban-cli --host=localhost --port=6980 --streamname=Command1
```

### Environment Variables

example .envrc:

```env
#!/usr/bin/env bash

export VBAN_CLI_HOST="localhost"
export VBAN_CLI_PORT=6980
export VBAN_CLI_STREAMNAME=Command1
```

---

## Use

*To be completed*

---

## License

`vban-cli` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
