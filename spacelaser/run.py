from .space_cannon import TargetPanel
from .space_command import SpaceCommand
from .config import Config


def main():
    options = Config().parse()
    target_panel = TargetPanel(options["schematics"])
    window = SpaceCommand(target_panel, options)
    window.draw()
