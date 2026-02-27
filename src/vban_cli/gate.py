from typing import Annotated

from cyclopts import App, Argument, Parameter

from .context import Context
from .help import CustomHelpFormatter

app = App(name='gate', help_formatter=CustomHelpFormatter())


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
    """Get or set the knob of the specified gate.

    Parameters
    ----------
    new_knob : int, optional
        If provided, sets the knob to this value. If not provided, the current knob is printed.
    """
    if new_knob is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(ctx.client.strip[index].gate.knob)
        return
    ctx.client.strip[index].gate.knob = new_knob


@app.command(name='threshold')
def threshold(
    new_threshold: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the threshold of the specified gate.

    Parameters
    ----------
    new_threshold : float, optional
        If provided, sets the threshold to this value. If not provided, the current threshold is printed.
    """
    if new_threshold is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(ctx.client.strip[index].gate.threshold)
        return
    ctx.client.strip[index].gate.threshold = new_threshold
