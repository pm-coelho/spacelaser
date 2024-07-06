from spacemenu.window import Window

from .space_cannon import TargetPanel, Cluster


class SpaceCommand:
    def __init__(self, panel: TargetPanel, options: dict):
        self.panel = panel
        self._root_window = Window(self._parse_panel(panel), options)

    def _parse_panel(self, targets: Cluster) -> dict:
        return {
            "label": "spacelaser",
            "branches": self._parse_clusters(targets.clusters),
            "leaves": self._parse_triggers(targets.triggers),
        }

    def _parse_clusters(self, chambers: list) -> list:
        return [
            {
                "label": c.label,
                "branches": self._parse_clusters(c.clusters),
                "leaves": self._parse_triggers(c.triggers),
            }
            for c in chambers
        ]

    def _parse_triggers(self, triggers: list) -> list:
        return [
            {
                "label": t.label,
                "command": t.command,
            }
            for t in triggers
        ]

    def draw(self):
        self._root_window.draw()
