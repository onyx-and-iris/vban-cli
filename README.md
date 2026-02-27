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

```console
Usage: vban-cli COMMAND

╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────╮
│ bus          Control the bus parameters.                                                         │
│ strip        Control the strip parameters.                                                       │
│ --help (-h)  Display this message and exit.                                                      │
│ --version    Display application version.                                                        │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Parameters ─────────────────────────────────────────────────────────────────────────────────────╮
│ --kind        Kind of Voicemeeter [env var: VBAN_CLI_KIND] [default: potato]                     │
│ --host        VBAN host [env var: VBAN_CLI_HOST] [default: localhost]                            │
│ --port        VBAN port [env var: VBAN_CLI_PORT] [default: 6980]                                 │
│ --streamname  VBAN stream name [env var: VBAN_CLI_STREAMNAME] [default: Command1]                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
```

For every command and subcommand there exists a `--help` flag for further usage information.

---

## Implementation Notes

1. The VBAN TEXT subprotocol defines two packet structures [ident:0][ident-0] and [ident:1][ident-1]. Neither of them contain the data for Bus EQ parameters.
2. Packet structure with [ident:1][ident-1] is emitted by the VBAN server only on pdirty events. This means we do not receive the initial state of those parameters on initial subscription. Therefore any commands which are intended to fetch the value of parameters defined in packet [ident:1][ident-1] will not work in this CLI.


---

## License

`vban-cli` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
 


[ident-0]: https://github.com/onyx-and-iris/Voicemeeter-SDK/blob/3be2c1c36563afbd6df3da8436406c77d2cc1f10/VoicemeeterRemote.h#L896
[ident-1]: https://github.com/onyx-and-iris/Voicemeeter-SDK/blob/3be2c1c36563afbd6df3da8436406c77d2cc1f10/VoicemeeterRemote.h#L982