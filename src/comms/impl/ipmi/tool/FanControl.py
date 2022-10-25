"""
Spec for implementation of IPMITool raw commands for different vendors
"""
class FanControl:

    """
    Command to enable manual fan control using ipmitool raw
    enabled: bool if true commands enables manual controls, false disables manual control
    """
    def manual_fancontrol_toggle_command(self, enabled: bool) -> str:
        pass

    """
    Command to set fan speed using ipmitool raw
    speedHex: str pwm value as hex string. Value must be between 0x0 and 0x64
    """
    def fan_speed_command(self, speedHex: str) -> str:
        pass