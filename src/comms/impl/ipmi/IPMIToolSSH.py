from ast import Try
from shutil import ExecError
from paramiko import SSHClient
from comms.CommsSpec import CommsSpec
from comms.impl.ipmi.tool.FanControl import FanControl
from comms.impl.ipmi.tool.TempSensor import TempSensor
from comms.impl.ipmi.tool import shellutils
from paramiko.client import SSHClient


"""
CommsSPec implementation using impitool over ssh

requires impitool and sensors to be installed in target host
"""
class IPMIToolSSH(CommsSpec):
    
    def __init__(self, host: str, port: int, username: str, password: str, commands: FanControl, tempsensor: TempSensor, require_sudo=True, ipmitool="ipmitool") -> None:
        super().__init__()
        self._commands = commands
        self._tempsensor = tempsensor
        self.require_sudo = require_sudo
        self.ipmitool = ipmitool
        self._password = password
        self._client = SSHClient()
        self._client.load_system_host_keys()
        self._client.connect(host, port=port, username=username, password=password)

    def _impitool_raw_command(self, payload: str) -> str:
        return f'{self.ipmitool} raw {payload}'

    def _sudo_command(self, cmd: str) -> str:
        scaped_pwd = shellutils.scape_str(self._password)
        return f'echo {scaped_pwd} | sudo -S {cmd}'

    def _exec_cmd(self, cmd) -> bool:
        cmd = cmd if not self.require_sudo else self._sudo_command(cmd)
        return self._client.exec_command(cmd)

    def set_fanspeed(self, pwm: int) -> bool:
        if 100 >= pwm >= 0:
            # Make sure manual fancontrol is enabled
            cmd = self._impitool_raw_command(self._commands.manual_fancontrol_toggle_command(True))
            self._exec_cmd(cmd)
            cmd = self._impitool_raw_command(self._commands.fan_speed_command(hex(pwm)))
            self._exec_cmd(cmd)
            return True
        else:
            return False

    def get_temp_c(self) -> float:
        _, stdout, stderr = self._exec_cmd(self._tempsensor.get_cpu_temp_command());
        result = stdout.read().decode('utf-8')
        return self._tempsensor.parse_temp_response(result)