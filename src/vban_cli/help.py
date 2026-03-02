import re

from cyclopts.help import DefaultFormatter, HelpPanel
from rich.console import Console, ConsoleOptions


class BaseHelpFormatter(DefaultFormatter):
    """Base help formatter that provides common functionality."""

    def __call__(
        self, console: Console, options: ConsoleOptions, panel: HelpPanel
    ) -> None:
        """Render a help panel, filtering out hidden parameters from Parameters sections."""
        if panel.title == 'Parameters':
            filtered_entries = [
                entry
                for entry in panel.entries
                if not (
                    entry.names
                    and any(
                        param in name.lower()
                        for name in entry.names
                        for param in self.get_filtered_params()
                    )
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

    def get_filtered_params(self):
        """Return list of parameter names to filter out of help output."""
        return ['index', 'band', 'ctx', 'target', 'eq_kind']


class StripHelpFormatter(BaseHelpFormatter):
    """Help formatter for strip commands that injects <index> after 'strip'."""

    def render_usage(self, console: Console, options: ConsoleOptions, usage) -> None:
        """Render the usage line with index argument injected after 'strip'.

        Handles both command groups (COMMAND) and individual commands (commandname [ARGS/OPTIONS]).
        """
        if usage:
            modified_usage = re.sub(
                r'(\S+\s+strip)\s+(\w+\s+\[[^\]]+\]|\w+\s+\[[^\]]+\]|\w+(?:\s+\[[^\]]+\])*|COMMAND)',
                r'\1 <index> \2',
                str(usage),
            )
            if modified_usage == str(usage):
                modified_usage = re.sub(
                    r'(\S+\s+strip)\s+(\w+)', r'\1 <index> \2', str(usage)
                )
            console.print(f'[bold]Usage:[/bold] {modified_usage}')


class BusHelpFormatter(BaseHelpFormatter):
    """Help formatter for bus commands that injects <index> after 'bus'."""

    def render_usage(self, console: Console, options: ConsoleOptions, usage) -> None:
        """Render the usage line with index argument injected after 'bus'.

        Handles both command groups (COMMAND) and individual commands (commandname [ARGS/OPTIONS])."""
        if usage:
            modified_usage = re.sub(
                r'(\S+\s+bus)\s+(\w+\s+\[[^\]]+\]|\w+\s+\[[^\]]+\]|\w+(?:\s+\[[^\]]+\])*|COMMAND)',
                r'\1 <index> \2',
                str(usage),
            )
            if modified_usage == str(usage):
                modified_usage = re.sub(
                    r'(\S+\s+bus)\s+(\w+)', r'\1 <index> \2', str(usage)
                )
            console.print(f'[bold]Usage:[/bold] {modified_usage}')


class EqHelpFormatter(BaseHelpFormatter):
    """Help formatter for eq commands that works with both strip and bus commands.

    Injects <index> after 'strip' or 'bus' and <band> after 'cell'."""

    def render_usage(self, console: Console, options: ConsoleOptions, usage) -> None:
        """Render the usage line with proper <index> placement for both strip and bus commands."""
        if usage:
            modified_usage = re.sub(
                r'(\S+\s+)(\w+)(\s+eq\s+)(COMMAND)', r'\1\2 <index>\3\4', str(usage)
            )
            console.print(f'[bold]Usage:[/bold] {modified_usage}')


class GainlayerHelpFormatter(BaseHelpFormatter):
    """Help formatter for gainlayer commands that works with strip commands.

    Injects <index> after 'strip' and <gainlayer_index> after 'gainlayer'."""

    def render_usage(self, console: Console, options: ConsoleOptions, usage) -> None:
        """Render the usage line with proper <index> placement for strip commands."""
        if usage:
            modified_usage = re.sub(
                r'(\S+\s+strip)(\s+gainlayer\s+)(COMMAND)',
                r'\1 <index>\2<[cyan]gainlayer_index[/cyan]> \3',
                str(usage),
            )
            console.print(f'[bold]Usage:[/bold] {modified_usage}')


class CellHelpFormatter(BaseHelpFormatter):
    """Help formatter for cell commands that works with both strip and bus commands.

    Injects <index> after 'strip' or 'bus' and <band> after 'cell'."""

    def render_usage(self, console: Console, options: ConsoleOptions, usage) -> None:
        """Render the usage line with proper <index> and <band> placement."""
        if usage:
            modified_usage = re.sub(
                r'(\S+\s+)(\w+)(\s+eq\s+cell\s+)(COMMAND)',
                r'\1\2 <index>\3<[cyan]band[/cyan]> \4',
                str(usage),
            )
            console.print(f'[bold]Usage:[/bold] {modified_usage}')
