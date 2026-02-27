# vmr-cli

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

---

## Install

#### With uv

```console
uv tool install vmr-cli
```

#### With pipx

```console
pipx install vmr-cli
```

The CLI should now be discoverable as `vmr-cli`

---

## Configuration

### Flags

```console
vmr-cli --host=localhost --port=6980 --streamname=Command1
```

### Environment Variables

example .envrc:

```env
#!/usr/bin/env bash

export VMR_CLI_HOST="localhost"
export VMR_CLI_PORT=6980
export VMR_CLI_STREAMNAME=Command1
```

---

## Use

*To be completed*

---

## License

`vmr-cli` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
