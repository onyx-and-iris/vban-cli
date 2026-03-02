from typing import Annotated

from cyclopts import App, Argument, Parameter

from . import console
from .context import Context
from .help import GainlayerHelpFormatter

app = App(name='gainlayer', help_formatter=GainlayerHelpFormatter())


@app.meta.default
def launcher(
    gainlayer_index: Annotated[int, Argument()],
    /,
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Control the gainlayers."""
    additional_kwargs = {}
    command, bound, _ = app.parse_args(tokens)
    additional_kwargs['strip_index'] = index
    additional_kwargs['gainlayer_index'] = gainlayer_index
    additional_kwargs['ctx'] = ctx

    return command(*bound.args, **bound.kwargs, **additional_kwargs)


@app.command(name='level')
def level(
    new_level: Annotated[float, Argument()] = None,
    *,
    strip_index: Annotated[int, Parameter(parse=False)],
    gainlayer_index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the level of the specified gainlayer.

    Parameters
    ----------
    new_level : float
        If provided, sets the level to this value. If not provided, the current level is printed.
    """
    if new_level is None:
        console.out.print(ctx.client.strip[strip_index].gainlayer[gainlayer_index].gain)
        return
    ctx.client.strip[strip_index].gainlayer[gainlayer_index].gain = new_level
