from pathlib import Path
from typing import Annotated

from cyclopts import App, Parameter, validators

from . import console, validation
from .context import Context
from .help import BaseHelpFormatter

app = App(name='recorder', help_formatter=BaseHelpFormatter())


@app.command(name='play')
def play(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Start the recorder playback."""
    ctx.client.recorder.play()
    console.out.print('Recorder playback started.')


@app.command(name='stop')
def stop(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Stop the recorder playback."""
    ctx.client.recorder.stop()
    console.out.print('Recorder playback stopped.')


@app.command(name='pause')
def pause(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Pause the recorder playback."""
    ctx.client.recorder.pause()
    console.out.print('Recorder playback paused.')


@app.command(name='replay')
def replay(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Replay the recorder playback."""
    ctx.client.recorder.replay()
    console.out.print('Recorder playback replay started.')


@app.command(name='record')
def record(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Start recording."""
    ctx.client.recorder.record()
    console.out.print('Recording started.')


@app.command(name='ff')
def ff(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Fast forward the recorder playback."""
    ctx.client.recorder.ff()
    console.out.print('Recorder playback fast forwarded.')


@app.command(name='rew')
def rew(
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Rewind the recorder playback."""
    ctx.client.recorder.rew()
    console.out.print('Recorder playback rewound.')


@app.command(name='load')
def load(
    file_path: Annotated[
        Path,
        Parameter(
            help='The path to the recording file to load.',
            validator=validators.Path(exists=True),
        ),
    ],
    /,
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Load a file into the recorder.

    note: This command may only work if vban-cli is running on localhost and may not work if vban-cli is running on a remote server."""
    ctx.client.recorder.load(file_path)
    console.out.print(f'Loaded file: {file_path}')


@app.command(name='goto')
def goto(
    time_string: Annotated[
        str,
        Parameter(
            help='The timestamp to go to in the recorder playback (format: HH:MM:SS).',
            validator=validation.is_valid_time_string,
        ),
    ],
    /,
    *,
    ctx: Annotated[Context, Parameter(show=False)] = None,
):
    """Go to a specific timestamp in the recorder playback."""
    ctx.client.recorder.goto(time_string)
    console.out.print(f'Went to timestamp {time_string} in recorder playback.')
