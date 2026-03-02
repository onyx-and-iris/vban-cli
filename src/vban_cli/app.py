from dataclasses import dataclass
from typing import Annotated

import vban_cmd
from cyclopts import App, Argument, Parameter, config
from rich.traceback import install as install_rich_traceback

from . import __version__ as version
from . import bus, command, console, recorder, strip
from .context import Context
from .error import VbanCLIConnectionError

app = App(
    config=config.Env(
        'VBAN_CLI_',
    ),  # Environment variable prefix for configuration parameters
    version=version,
    console=console.out,
    error_console=console.err,
    exit_on_error=True,
)
app.command(strip.app.meta, name='strip')
app.command(bus.app.meta, name='bus')
app.command(command.app, name='command')
app.command(recorder.app, name='recorder')
app.register_install_completion_command()

install_rich_traceback(console=console.err)


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

    try:
        with vban_cmd.api(
            vban_config.kind,
            host=vban_config.host,
            port=vban_config.port,
            streamname=vban_config.streamname,
            disable_rt_listeners=disable_rt_listeners,
        ) as client:
            return command(*bound.args, **bound.kwargs, ctx=Context(client=client))
    except vban_cmd.error.VBANCMDConnectionError as e:
        raise VbanCLIConnectionError(str(e)) from e


@app.command(name='sendtext')
def sendtext(
    text: Annotated[str, Argument()],
    /,
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Send a text command to the current Voicemeeter/Matrix instance."""
    if resp := ctx.client.sendtext(text):
        app.console.print(resp)


def run():
    app.meta()
