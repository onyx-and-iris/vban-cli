from typing import Annotated, Optional

from cyclopts import App, Argument, Parameter

from . import comp, console, denoiser, eq, gate
from .context import Context
from .help import CustomHelpFormatter

app = App(name='strip', help_formatter=CustomHelpFormatter())
app.command(eq.app.meta, name='eq')
app.command(comp.app.meta, name='comp')
app.command(gate.app.meta, name='gate')
app.command(denoiser.app.meta, name='denoiser')


@app.meta.default
def launcher(
    index: Annotated[int, Argument()] = None,
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Control the strip parameters."""
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
    new_state: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the mono state of the specified strip.

    Parameters
    ----------
    new_state : bool, optional
        If provided, sets the mono state to this value. If not provided, the current mono state is printed.
    """
    if new_state is None:
        console.out.print(ctx.client.strip[index].mono)
        return
    ctx.client.strip[index].mono = new_state


@app.command(name='solo')
def solo(
    new_state: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the solo state of the specified strip.

    Parameters
    ----------
    new_state : bool, optional
        If provided, sets the solo state to this value. If not provided, the current solo state is printed.
    """
    if new_state is None:
        console.out.print(ctx.client.strip[index].solo)
        return
    ctx.client.strip[index].solo = new_state


@app.command(name='mute')
def mute(
    new_state: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the mute state of the specified strip.

    Parameters
    ----------
    new_state : bool, optional
        If provided, sets the mute state to this value. If not provided, the current mute state is printed.
    """
    if new_state is None:
        console.out.print(ctx.client.strip[index].mute)
        return
    ctx.client.strip[index].mute = new_state


@app.command(name='gain')
def gain(
    new_value: Annotated[Optional[float], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the gain of the specified strip.

    Parameters
    ----------
    new_value : float, optional
        If provided, sets the gain to this value. If not provided, the current gain is printed.
    """
    if new_value is None:
        console.out.print(ctx.client.strip[index].gain)
        return
    ctx.client.strip[index].gain = new_value


@app.command(name='A1')
def a1(
    new_value: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the A1 state of the specified strip.

    Parameters
    ----------
    new_value : bool, optional
        If provided, sets the A1 state to this value. If not provided, the current A1 state is printed.
    """
    if new_value is None:
        console.out.print(ctx.client.strip[index].A1)
        return
    ctx.client.strip[index].A1 = new_value


@app.command(name='A2')
def a2(
    new_value: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the A2 state of the specified strip.

    Parameters
    ----------
    new_value : bool, optional
        If provided, sets the A2 state to this value. If not provided, the current A2 state is printed.
    """
    if new_value is None:
        console.out.print(ctx.client.strip[index].A2)
        return
    ctx.client.strip[index].A2 = new_value


@app.command(name='A3')
def a3(
    new_value: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the A3 state of the specified strip.

    Parameters
    ----------
    new_value : bool, optional
        If provided, sets the A3 state to this value. If not provided, the current A3 state is printed.
    """
    if new_value is None:
        console.out.print(ctx.client.strip[index].A3)
        return
    ctx.client.strip[index].A3 = new_value


@app.command(name='A4')
def a4(
    new_value: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the A4 state of the specified strip.

    Parameters
    ----------
    new_value : bool, optional
        If provided, sets the A4 state to this value. If not provided, the current A4 state is printed.
    """
    if new_value is None:
        console.out.print(ctx.client.strip[index].A4)
        return
    ctx.client.strip[index].A4 = new_value


@app.command(name='A5')
def a5(
    new_value: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the A5 state of the specified strip.

    Parameters
    ----------
    new_value : bool, optional
        If provided, sets the A5 state to this value. If not provided, the current A5 state is printed.
    """
    if new_value is None:
        console.out.print(ctx.client.strip[index].A5)
        return
    ctx.client.strip[index].A5 = new_value


@app.command(name='B1')
def b1(
    new_value: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the B1 state of the specified strip.

    Parameters
    ----------
    new_value : bool, optional
        If provided, sets the B1 state to this value. If not provided, the current B1 state is printed.
    """
    if new_value is None:
        console.out.print(ctx.client.strip[index].B1)
        return
    ctx.client.strip[index].B1 = new_value


@app.command(name='B2')
def b2(
    new_value: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the B2 state of the specified strip.

    Parameters
    ----------
    new_value : bool, optional
        If provided, sets the B2 state to this value. If not provided, the current B2 state is printed.
    """
    if new_value is None:
        console.out.print(ctx.client.strip[index].B2)
        return
    ctx.client.strip[index].B2 = new_value


@app.command(name='B3')
def b3(
    new_value: Annotated[Optional[bool], Argument()] = None,
    *,
    index: Annotated[int, Parameter(show=False)] = None,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Get or set the B3 state of the specified strip.

    Parameters
    ----------
    new_value : bool, optional
        If provided, sets the B3 state to this value. If not provided, the current B3 state is printed.
    """
    if new_value is None:
        console.out.print(ctx.client.strip[index].B3)
        return
    ctx.client.strip[index].B3 = new_value
