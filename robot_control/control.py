from typing import Literal

class Robot:
    def __init__(self, name):
        pass

    def get_obs(self):
        obs = {}
        return obs

    def move(self, action, action_type: Literal["joint", "ee", "delta_ee"] = "joint"):
        if action_type not in ("joint", "ee", "delta_ee"):
            raise ValueError(f"Invalid action_type: {action_type}")
        if action_type == "joint":
            pass
        elif action_type == "ee":
            pass
        elif action_type == "delta_ee":
            pass

    def reset_arm_pose(self):
        pass