"""
Spec to get command for temp sensor scan
"""
class TempSensor:
    
    """
    Command to get the cpu temp
    """
    def get_cpu_temp_command(self) -> str:
        pass

    """
    Parse get_cpu_temp_command result to get the temp in celcius
    """
    def parse_temp_response(self, res: str) -> float:
        pass
