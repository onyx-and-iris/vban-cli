from typing import Annotated

from cyclopts import App, Argument, Parameter

from .context import Context
from .help import StripSubcommandHelpFormatter

app = App(name='denoiser', help_formatter=StripSubcommandHelpFormatter())


@app.meta.default
def launcher(
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    index: Annotated[int, Argument()] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Control the denoiser parameters."""
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
    """Get or set the knob of the specified denoiser.

    Parameters
    ----------
    new_knob : int, optional
        If provided, sets the knob to this value. If not provided, the current knob is printed.
    """
    if new_knob is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(ctx.client.strip[index].denoiser.knob)
        return
    ctx.client.strip[index].denoiser.knob = new_knob
