from typing import Annotated

from cyclopts import App, Argument, Parameter

from .context import Context
from .help import StripHelpFormatter

app = App(name='gate', help_formatter=StripHelpFormatter())


@app.meta.default
def launcher(
    *tokens: Annotated[str, Parameter(show=False, allow_leading_hyphen=True)],
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Control the compressor parameters."""
    additional_kwargs = {}
    command, bound, _ = app.parse_args(tokens)
    additional_kwargs['index'] = index
    additional_kwargs['ctx'] = ctx

    return command(*bound.args, **bound.kwargs, **additional_kwargs)


@app.command(name='knob')
def knob(
    new_knob: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the knob of the specified gate.

    Parameters
    ----------
    new_knob : int, optional
        If provided, sets the knob to this value. If not provided, the current knob is printed.
    """
    if new_knob is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].gate.knob)
        return
    ctx.client.strip[index].gate.knob = new_knob


@app.command(name='threshold')
def threshold(
    new_threshold: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the threshold of the specified gate.

    Parameters
    ----------
    new_threshold : float, optional
        If provided, sets the threshold to this value. If not provided, the current threshold is printed.
    """
    if new_threshold is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].gate.threshold)
        return
    ctx.client.strip[index].gate.threshold = new_threshold


@app.command(name='damping-max')
def damping_max(
    new_damping_max: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the damping max of the specified gate.

    Parameters
    ----------
    new_damping_max : float, optional
        If provided, sets the damping max to this value. If not provided, the current damping max is printed.
    """
    if new_damping_max is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].gate.damping)
        return
    ctx.client.strip[index].gate.damping = new_damping_max


@app.command(name='bp-sidechain')
def bp_sidechain(
    new_bp_sidechain: Annotated[bool, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the BP sidechain of the specified gate.

    Parameters
    ----------
    new_bp_sidechain : bool, optional
        If provided, sets the BP sidechain to this value. If not provided, the current BP sidechain is printed.
    """
    if new_bp_sidechain is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].gate.bpsidechain)
        return
    ctx.client.strip[index].gate.bpsidechain = new_bp_sidechain


@app.command(name='attack')
def attack(
    new_attack: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the attack of the specified gate.

    Parameters
    ----------
    new_attack : float, optional
        If provided, sets the attack to this value. If not provided, the current attack is printed.
    """
    if new_attack is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].gate.attack)
        return
    ctx.client.strip[index].gate.attack = new_attack


@app.command(name='hold')
def hold(
    new_hold: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the hold of the specified gate.

    Parameters
    ----------
    new_hold : float, optional
        If provided, sets the hold to this value. If not provided, the current hold is printed.
    """
    if new_hold is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].gate.hold)
        return
    ctx.client.strip[index].gate.hold = new_hold


@app.command(name='release')
def release(
    new_release: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the release of the specified gate.

    Parameters
    ----------
    new_release : float, optional
        If provided, sets the release to this value. If not provided, the current release is printed.
    """
    if new_release is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].gate.release)
        return
    ctx.client.strip[index].gate.release = new_release
