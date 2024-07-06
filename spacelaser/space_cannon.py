import yaml


class Node:
    def __init__(self, label, targets=None, command=None):
        self.label = label
        self.targets = targets
        self.command = command


class Cluster(Node):
    def __init__(self, label, targets):
        super(Cluster, self).__init__(label, targets=targets)
        self.clusters = []
        self.triggers = []

        self.load_cluster(targets)

    def load_cluster(self, targets):
        if not targets:
            raise ValueError("Targets not loaded")

        for target in targets:
            if target.get("command"):
                self.triggers.append(
                    Trigger(target["label"], command=target["command"])
                )
            else:
                self.clusters.append(Cluster(target["label"], target["clusters"]))


class TargetPanel(Cluster):
    def __init__(self, schematics_path):
        self.schematics = self.load_schematics(schematics_path)
        targets = self.parse_targets(self.schematics["targets"])
        super(TargetPanel, self).__init__("Space Command", targets)

    def load_schematics(self, schematics_path: str) -> dict:
        with open(schematics_path, "r") as f:
            schematics = yaml.safe_load(f)

            if not schematics:
                raise ValueError("Schematics not loaded")
            if not schematics.get("targets"):
                raise ValueError("Clusters not loaded")

        return schematics

    def parse_targets(self, targets):
        parsed_targets = []
        for label, sub_targets in targets.items():
            if isinstance(sub_targets, dict):
                parsed_targets.append(
                    {
                        "label": label,
                        "clusters": self.parse_targets(sub_targets),
                    }
                )
            else:
                parsed_targets.append(
                    {
                        "label": label,
                        "command": sub_targets,
                    }
                )
        return parsed_targets


class Trigger(Node):
    def __init__(self, label, command):
        super(Trigger, self).__init__(label, command=command)
