from pathlib import Path
from typing import Annotated

from cyclopts import App, Parameter, validators

from . import validation
from .context import Context
from .help import BaseHelpFormatter

app = App(
    name='recorder',
    help='Control the recorder playback and recording',
    help_formatter=BaseHelpFormatter(),
)


@app.command(name='play')
def play(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Start the recorder playback."""
    ctx.client.recorder.play()
    app.console.print('Recorder playback started.')


@app.command(name='pause')
def pause(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Pause the recorder playback."""
    ctx.client.recorder.stop()
    app.console.print('Recorder playback paused.')


@app.command(name='stop')
def stop(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Stop the recorder playback/recording and reset to the beginning."""
    ctx.client.recorder.stop()
    ctx.client.recorder.goto('00:00:00')
    # We have no way of knowing if the recorder was playing or recording, so we print a generic message.
    # See https://github.com/onyx-and-iris/vban-cli?tab=readme-ov-file#implementation-notes - 4.
    app.console.print('Recorder stopped.')


@app.command(name='replay')
def replay(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Replay the recorder playback."""
    ctx.client.recorder.replay()
    app.console.print('Recorder playback replay started.')


@app.command(name='record')
def record(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Start recording."""
    ctx.client.recorder.record()
    app.console.print('Recorder recording started.')


@app.command(name='pause-recording')
def pause_recording(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Pause the recorder recording."""
    ctx.client.recorder.pause()
    app.console.print('Recorder recording paused.')


@app.command(name='ff')
def ff(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Fast forward the recorder playback."""
    ctx.client.recorder.ff()
    app.console.print('Recorder playback fast forwarded.')


@app.command(name='rew')
def rew(
    *,
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Rewind the recorder playback."""
    ctx.client.recorder.rew()
    app.console.print('Recorder playback rewound.')


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
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Load a file into the recorder.

    note: This command may only work if vban-cli is running on localhost and may not work if vban-cli is running on a remote server."""
    ctx.client.recorder.load(file_path)
    app.console.print(f'Loaded file: {file_path}')


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
    ctx: Annotated[Context, Parameter(parse=False)],
):
    """Go to a specific timestamp in the recorder playback."""
    ctx.client.recorder.goto(time_string)
    app.console.print(f'Went to timestamp {time_string} in recorder playback.')
