from typing import Annotated

from cyclopts import App, Parameter

from .context import Context
from .help import BaseHelpFormatter

app = App(
    name='command',
    help='Execute commands that perform actions',
    help_formatter=BaseHelpFormatter(),
)


@app.command(name='show')
def show(
    *,
    ctx: Annotated[Context, Parameter(parse=False)] = None,
):
    """Bring the Voicemeeter GUI to the foreground."""
    ctx.client.command.show()
    app.console.print('Voicemeeter GUI should now be in the foreground.')


@app.command(name='hide')
def hide(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Send the Voicemeeter GUI to the background."""
    ctx.client.command.hide()
    app.console.print('Voicemeeter GUI should now be in the background.')


@app.command(name='shutdown')
def shutdown(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Shut down Voicemeeter."""
    ctx.client.command.shutdown()
    app.console.print('Voicemeeter should now be shut down.')


@app.command(name='restart')
def restart(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Restart the Voicemeeter engine."""
    ctx.client.command.restart()
    app.console.print('Voicemeeter engine should now be restarting.')


@app.command(name='lock')
def lock(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Lock the Voicemeeter GUI."""
    ctx.client.command.lock = True
    app.console.print('Voicemeeter GUI should now be locked.')


@app.command(name='unlock')
def unlock(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Unlock the Voicemeeter GUI."""
    ctx.client.command.lock = False
    app.console.print('Voicemeeter GUI should now be unlocked.')
