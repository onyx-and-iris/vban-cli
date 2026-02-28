from typing import Annotated

from cyclopts import App, Argument, Parameter

from .context import Context
from .help import CellHelpFormatter, EqHelpFormatter

cell_app = App(name='cell', help_formatter=CellHelpFormatter())

app = App(name='eq', help_formatter=EqHelpFormatter())
app.command(cell_app.meta, name='cell')


@app.meta.default
def launcher(
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    eq_kind: Annotated[str, Parameter(show=False)] = None,
    index: Annotated[int, Argument()] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Control the EQ parameters."""
    additional_kwargs = {}
    command, bound, _ = app.parse_args(tokens)
    match eq_kind:
        case 'strip':
            target = ctx.client.strip[index].eq
        case 'bus':
            target = ctx.client.bus[index].eq
        case _:
            raise ValueError(f'Invalid eq_kind: {eq_kind}')
    additional_kwargs['target'] = target

    return command(*bound.args, **bound.kwargs, **additional_kwargs)


@app.command(name='on')
def on(
    new_state: Annotated[bool, Argument()] = None,
    *,
    target: Annotated[object, Parameter(show=False)] = None,
):
    """Get or set the on state of the specified EQ band.

    Parameters
    ----------
    new_state : bool
        If provided, sets the on state to this value. If not provided, the current on state is printed.
    """
    if new_state is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(target.on)
        return
    target.on = new_state


@cell_app.meta.default
def cell_launcher(
    band: Annotated[int, Argument()] = None,
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    target: Annotated[object, Parameter(show=False)] = None,
):
    """Control the EQ Cell parameters.

    Only channel 0 is supported, see https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 3.
    """
    additional_kwargs = {}
    command, bound, _ = app.parse_args(tokens)
    additional_kwargs['target'] = target.channel[0].cell[band]

    return command(*bound.args, **bound.kwargs, **additional_kwargs)


@cell_app.command(name='on')
def cell_on(
    new_state: Annotated[bool, Argument()] = None,
    *,
    target: Annotated[object, Parameter(show=False)] = None,
):
    """Get or set the on state of the specified EQ cell.

    Parameters
    ----------
    new_state : bool
        If provided, sets the on state to this value. If not provided, the current on state is printed.
    """
    if new_state is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(target.on)
        return
    target.on = new_state
