from dataclasses import dataclass

from vban_cmd.vbancmd import VbanCmd


@dataclass
class Context:
    client: VbanCmd
