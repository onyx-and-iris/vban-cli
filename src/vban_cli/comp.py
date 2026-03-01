from typing import Annotated

from cyclopts import App, Argument, Parameter

from .context import Context
from .help import StripHelpFormatter

app = App(name='comp', help_formatter=StripHelpFormatter())


@app.meta.default
def launcher(
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    index: Annotated[int, Argument()] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Control the compressor parameters."""
    additional_kwargs = {}
    command, bound, _ = app.parse_args(tokens)
    if index is not None:
        additional_kwargs['index'] = index
    if ctx is not None:
        additional_kwargs['ctx'] = ctx

    return command(*bound.args, **bound.kwargs, **additional_kwargs)


@app.command(name='knob')
def knob(
    new_knob: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the knob of the specified compressor.

    Parameters
    ----------
    new_knob : int, optional
        If provided, sets the knob to this value. If not provided, the current knob is printed.
    """
    if new_knob is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(ctx.client.strip[index].comp.knob)
        return
    ctx.client.strip[index].comp.knob = new_knob


@app.command(name='input-gain')
def input_gain(
    new_gain: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the input gain of the specified compressor.

    Parameters
    ----------
    new_gain : float, optional
        If provided, sets the input gain to this value. If not provided, the current input gain is printed.
    """
    if new_gain is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(ctx.client.strip[index].comp.gainin)
        return
    ctx.client.strip[index].comp.gainin = new_gain
