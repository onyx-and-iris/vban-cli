from dataclasses import dataclass
from typing import Annotated

import vban_cmd
from cyclopts import App, Argument, Parameter, config

from . import __version__ as version
from . import bus, console, strip
from .context import Context

app = App(
    config=config.Env(
        'VBAN_CLI_',
    ),  # Environment variable prefix for configuration parameters
    version=version,
)
app.command(strip.app.meta, name='strip')
app.command(bus.app.meta, name='bus')
app.register_install_completion_command()


@Parameter(name='*')
@dataclass
class VBANConfig:
    kind: Annotated[str, Parameter(help='Kind of Voicemeeter')] = 'potato'
    host: Annotated[str, Parameter(help='VBAN host')] = 'localhost'
    port: Annotated[int, Parameter(help='VBAN port')] = 6980
    streamname: Annotated[str, Parameter(help='VBAN stream name')] = 'Command1'


@app.meta.default
def launcher(
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    vban_config: Annotated[VBANConfig, Parameter()] = VBANConfig(),
):
    command, bound, _ = app.parse_args(tokens)
    if tokens[0] == '--install-completion':
        return command(*bound.args, **bound.kwargs)

    disable_rt_listeners = False
    if command.__name__ == 'sendtext':
        disable_rt_listeners = True

    with vban_cmd.api(
        vban_config.kind,
        ip=vban_config.host,
        port=vban_config.port,
        streamname=vban_config.streamname,
        disable_rt_listeners=disable_rt_listeners,
    ) as client:
        return command(*bound.args, **bound.kwargs, ctx=Context(client=client))


@app.command(name='sendtext')
def sendtext(
    text: Annotated[str, Argument()],
    /,
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Send a text command to the current Voicemeeter/Matrix instance."""
    if resp := ctx.client.sendtext(text):
        console.out.print(resp)


def run():
    try:
        app.meta()
    except Exception as e:
        console.err.print(f'Error: {e}')
        return e.code
