import re

from cyclopts.help import DefaultFormatter, HelpPanel
from rich.console import Console, ConsoleOptions


class CustomHelpFormatter(DefaultFormatter):
    """Custom help formatter that injects an index argument into the usage line and filters it out from the parameters list.

    This formatter modifies the usage line to include an <index> argument after the 'strip' command,
    and filters out any parameters related to 'index' from the Parameters section of the help output.
    """

    def render_usage(self, console: Console, options: ConsoleOptions, usage) -> None:
        """Render the usage line with index argument injected."""
        if usage:
            modified_usage = re.sub(
                r'(\S+\s+[a-z]+)\s+(COMMAND)', r'\1 <index> \2', str(usage)
            )
            console.print(f'[bold]Usage:[/bold] {modified_usage}')

    def __call__(
        self, console: Console, options: ConsoleOptions, panel: HelpPanel
    ) -> None:
        """Render a help panel, filtering out the index parameter from Parameters sections."""
        if panel.title == 'Parameters':
            filtered_entries = [
                entry
                for entry in panel.entries
                if not (
                    entry.names and any('index' in name.lower() for name in entry.names)
                )
            ]

            filtered_panel = HelpPanel(
                title=panel.title,
                entries=filtered_entries,
                description=panel.description,
                format=panel.format,
            )
            super().__call__(console, options, filtered_panel)
        else:
            super().__call__(console, options, panel)
