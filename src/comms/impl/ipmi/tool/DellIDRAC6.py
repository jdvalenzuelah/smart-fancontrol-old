from comms.impl.ipmi.tool.FanControl import FanControl


from comms.impl.ipmi.tool.FanControl import FanControl

"""
impitool fan control raw commands for dell's IDrac6. Tested on Poweredge R210
"""
class DellIDRAC6(FanControl):
    def manual_fancontrol_toggle_command(self, enabled: bool) -> str:
        toggle = '0x00' if enabled else '0x01'
        return f'0x30 0x30 0x01 {toggle}'

    def fan_speed_command(self, speedHex: str) -> str:
        return f'0x30 0x30 0x02 0xff {speedHex}'
