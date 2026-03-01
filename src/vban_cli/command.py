from typing import Annotated

from cyclopts import App, Parameter

from . import console
from .context import Context
from .help import BaseHelpFormatter

app = App(name='command', help_formatter=BaseHelpFormatter())


@app.command(name='show')
def show(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Bring the Voicemeeter GUI to the foreground."""
    ctx.client.command.show()
    console.out.print('Voicemeeter GUI should now be in the foreground.')


@app.command(name='hide')
def hide(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Send the Voicemeeter GUI to the background."""
    ctx.client.command.hide()
    console.out.print('Voicemeeter GUI should now be in the background.')


@app.command(name='shutdown')
def shutdown(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Shut down Voicemeeter."""
    ctx.client.command.shutdown()
    console.out.print('Voicemeeter should now be shut down.')


@app.command(name='restart')
def restart(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Restart the Voicemeeter engine."""
    ctx.client.command.restart()
    console.out.print('Voicemeeter engine should now be restarting.')
