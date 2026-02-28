# vban-cli

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

---

This CLI is still in an early stage of development with many more things that could be implemented. However, the commands that are implemented should be working without issues.

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

### Strip Command

Usage: vban-cli strip <index> COMMAND [ARGS]

examples:

```console
vban-cli strip 0 mute true

vban-cli strip 1 A1 true

vban-cli strip 2 gain -18.7
```

see `vban-cli strip --help` for more info.

### Bus Command

Usage: vban-cli bus <index> COMMAND [ARGS]

examples:

```console
vban-cli bus mode normal

vban-cli bus mute true
```

see `vban-cli bus --help` for more info.

---

## Implementation Notes

1. The VBAN TEXT subprotocol defines two packet structures [ident:0][ident-0] and [ident:1][ident-1]. Neither of them contain the data for Bus EQ parameters.
2. Packet structure with [ident:1][ident-1] is emitted by the VBAN server only on pdirty events. This means we do not receive the initial state of those parameters on initial subscription. Therefore any commands which are intended to fetch the value of parameters defined in packet [ident:1][ident-1] will not work in this CLI.
3. Packet structure with [ident:1][ident-1] defines parameteric EQ data only for the [first channel][ident-1-peq].

---

## Further Notes

I've made the effort to set up the basic skeletal structure of the CLI as well as demonstrate how to combine subcommand groups with subcommand groups so more can be implemented, it just needs doing. There may be restrictions on some things however, for example, retrieving values is only possible for parameters [defined in the protocol](https://github.com/onyx-and-iris/Voicemeeter-SDK/blob/3be2c1c36563afbd6df3da8436406c77d2cc1f10/VoicemeeterRemote.h#L787). Setting parameters can be done for anything possible by a string request.

Shell completion scripts are available (for zsh, bash and fish) but I haven't tested them

Some of the help output needs improving for commands that branch off positional arguments.

If there's something missing that you would like to see added the best bet is to submit a PR. You may raise an issue and if it's quick and simple to do I may (or may not) do it.

---

## License

`vban-cli` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
 


[ident-0]: https://github.com/onyx-and-iris/Voicemeeter-SDK/blob/3be2c1c36563afbd6df3da8436406c77d2cc1f10/VoicemeeterRemote.h#L896
[ident-1]: https://github.com/onyx-and-iris/Voicemeeter-SDK/blob/3be2c1c36563afbd6df3da8436406c77d2cc1f10/VoicemeeterRemote.h#L982
[ident-1-peq]: https://github.com/onyx-and-iris/Voicemeeter-SDK/blob/3be2c1c36563afbd6df3da8436406c77d2cc1f10/VoicemeeterRemote.h#L995