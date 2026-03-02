from typing import Annotated

from cyclopts import App, Argument, Parameter

from .context import Context
from .help import StripHelpFormatter

app = App(name='comp', help_formatter=StripHelpFormatter())


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
    """Get or set the knob of the specified compressor.

    Parameters
    ----------
    new_knob : int, optional
        If provided, sets the knob to this value. If not provided, the current knob is printed.
    """
    if new_knob is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].comp.knob)
        return
    ctx.client.strip[index].comp.knob = new_knob


@app.command(name='input-gain')
def input_gain(
    new_gain: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the input gain of the specified compressor.

    Parameters
    ----------
    new_gain : float, optional
        If provided, sets the input gain to this value. If not provided, the current input gain is printed.
    """
    if new_gain is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].comp.gainin)
        return
    ctx.client.strip[index].comp.gainin = new_gain


@app.command(name='ratio')
def ratio(
    new_ratio: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the ratio of the specified compressor.

    Parameters
    ----------
    new_ratio : float, optional
        If provided, sets the ratio to this value. If not provided, the current ratio is printed.
    """
    if new_ratio is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].comp.ratio)
        return
    ctx.client.strip[index].comp.ratio = new_ratio


@app.command(name='threshold')
def threshold(
    new_threshold: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the threshold of the specified compressor.

    Parameters
    ----------
    new_threshold : float, optional
        If provided, sets the threshold to this value. If not provided, the current threshold is printed.
    """
    if new_threshold is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].comp.threshold)
        return
    ctx.client.strip[index].comp.threshold = new_threshold


@app.command(name='attack')
def attack(
    new_attack: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the attack of the specified compressor.

    Parameters
    ----------
    new_attack : float, optional
        If provided, sets the attack to this value. If not provided, the current attack is printed.
    """
    if new_attack is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].comp.attack)
        return
    ctx.client.strip[index].comp.attack = new_attack


@app.command(name='release')
def release(
    new_release: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the release of the specified compressor.

    Parameters
    ----------
    new_release : float, optional
        If provided, sets the release to this value. If not provided, the current release is printed.
    """
    if new_release is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].comp.release)
        return
    ctx.client.strip[index].comp.release = new_release


@app.command(name='knee')
def knee(
    new_knee: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the knee of the specified compressor.

    Parameters
    ----------
    new_knee : float, optional
        If provided, sets the knee to this value. If not provided, the current knee is printed.
    """
    if new_knee is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].comp.knee)
        return
    ctx.client.strip[index].comp.knee = new_knee


@app.command(name='output-gain')
def output_gain(
    new_gain: Annotated[float, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the output gain of the specified compressor.

    Parameters
    ----------
    new_gain : float, optional
        If provided, sets the output gain to this value. If not provided, the current output gain is printed.
    """
    if new_gain is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].comp.gainout)
        return
    ctx.client.strip[index].comp.gainout = new_gain


@app.command(name='auto-makeup')
def makeup(
    new_makeup: Annotated[bool, Argument()] = None,
    *,
    index: Annotated[int, Parameter(parse=False)],
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Get or set the auto-makeup of the specified compressor.

    Parameters
    ----------
    new_makeup : bool, optional
        If provided, sets the auto-makeup to this value. If not provided, the current auto-makeup is printed.
    """
    if new_makeup is None:
        # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 2.
        # app.console.print(ctx.client.strip[index].comp.makeup)
        return
    ctx.client.strip[index].comp.makeup = new_makeup
