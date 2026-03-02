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
    command, bound, _ = cell_app.parse_args(tokens)
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


@cell_app.command(name='freq')
def cell_freq(
    new_freq: Annotated[float, Argument()] = None,
    *,
    target: Annotated[object, Parameter(show=False)] = None,
):
    """Get or set the frequency of the specified EQ cell.

    Parameters
    ----------
    new_freq : float
        If provided, sets the frequency to this value. If not provided, the current frequency is printed.
    """
    if new_freq is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(target.f)
        return
    target.f = new_freq


@cell_app.command(name='gain')
def cell_gain(
    new_gain: Annotated[float, Argument()] = None,
    *,
    target: Annotated[object, Parameter(show=False)] = None,
):
    """Get or set the gain of the specified EQ cell.

    Parameters
    ----------
    new_gain : float
        If provided, sets the gain to this value. If not provided, the current gain is printed.
    """
    if new_gain is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(target.gain)
        return
    target.gain = new_gain


@cell_app.command(name='quality')
def cell_q(
    new_q: Annotated[float, Argument()] = None,
    *,
    target: Annotated[object, Parameter(show=False)] = None,
):
    """Get or set the Q of the specified EQ cell.

    Parameters
    ----------
    new_q : float
        If provided, sets the Q to this value. If not provided, the current Q is printed.
    """
    if new_q is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(target.q)
        return
    target.q = new_q


@cell_app.command(name='type')
def cell_type(
    new_type: Annotated[int, Argument()] = None,
    *,
    target: Annotated[object, Parameter(show=False)] = None,
):
    """Get or set the type of the specified EQ cell.

    Parameters
    ----------
    new_type : int
        If provided, sets the type to this value. If not provided, the current type is printed.
    """
    if new_type is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # console.out.print(target.type)
        return
    target.type = new_type
