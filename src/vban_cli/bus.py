from typing import Annotated, Literal, Optional

from cyclopts import App, Argument, Parameter

from . import console
from .context import Context
from .help import BusHelpFormatter

app = App(name='bus', help_formatter=BusHelpFormatter())
# See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 1.
# app.command(eq.app.meta, name='eq')


@app.meta.default
def launcher(
    index: Annotated[int, Argument()] = None,
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Control the bus parameters."""
    additional_kwargs = {}
    command, bound, _ = app.parse_args(tokens)
    if tokens[0] == 'eq':
        additional_kwargs['eq_kind'] = app.name[0]
    if index is not None:
        additional_kwargs['index'] = index
    if ctx is not None:
        additional_kwargs['ctx'] = ctx

    return command(*bound.args, **bound.kwargs, **additional_kwargs)


@app.command(name='mono')
def mono(
    new_value: Annotated[
        Optional[Literal['off', 'mono', 'stereoreverse']], Argument()
    ] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the mono state of the specified bus.

    Parameters
    ----------
    new_value : {'off', 'mono', 'stereoreverse'}, optional
        If provided, sets the mono state to this value. If not provided, the current mono state is printed.
    """
    if new_value is None:
        console.out.print(['off', 'mono', 'stereoreverse'][ctx.client.bus[index].mono])
        return
    ctx.client.bus[index].mono = ['off', 'mono', 'stereoreverse'].index(new_value)


@app.command(name='mute')
def mute(
    new_value: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the mute state of the specified bus.

    Parameters
    ----------
    new_value : bool, optional
        If provided, sets the mute state to this value. If not provided, the current mute state is printed.
    """
    if new_value is None:
        console.out.print(ctx.client.bus[index].mute)
        return
    ctx.client.bus[index].mute = new_value


@app.command(name='mode')
def mode(
    type_: Annotated[
        Optional[
            Literal[
                'normal',
                'amix',
                'bmix',
                'repeat',
                'composite',
                'tvmix',
                'upmix21',
                'upmix41',
                'upmix61',
                'centeronly',
                'lfeonly',
                'rearonly',
            ]
        ],
        Argument(),
    ] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the bus mode of the specified bus.

    Parameters
    ----------
    type_ : str, optional
        If provided, sets the bus mode to this value. If not provided, the current bus mode is printed.
    """
    if type_ is None:
        console.out.print(ctx.client.bus[index].mode.get())
        return
    setattr(ctx.client.bus[index].mode, type_, True)
