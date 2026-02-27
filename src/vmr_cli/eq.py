from typing import Annotated

from cyclopts import App, Argument, Parameter

from .context import Context
from .help import CustomHelpFormatter

app = App(name='eq', help_formatter=CustomHelpFormatter())


@app.meta.default
def launcher(
    band: Annotated[int, Argument()] = None,
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    index: Annotated[int, Argument()] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Control the EQ parameters.

    Only channel 0 is supported, as the VBAN protocol only exposes parameters for this channel.
    """
    additional_kwargs = {}
    command, bound, _ = app.parse_args(tokens)
    if index is not None:
        additional_kwargs['index'] = index
    if band is not None:
        additional_kwargs['band'] = band
    if ctx is not None:
        additional_kwargs['ctx'] = ctx

    return command(*bound.args, **bound.kwargs, **additional_kwargs)


@app.command(name='on')
def on(
    new_state: Annotated[bool, Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    band: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the on state of the specified EQ band.

    Parameters
    ----------
    new_state : bool
        If provided, sets the on state to this value. If not provided, the current on state is printed.
    """
    if new_state is None:
        # This doesn't work because the VBAN protocol doesn't send an initial NBS1 packet.
        # console.out.print(ctx.client.strip[index].eq.channel[0].cell[band].on)
        return
    ctx.client.strip[index].eq.channel[0].cell[band].on = new_state
