import json
from comms.impl.ipmi.tool.TempSensor import TempSensor

"""
TempSensor commands using linux `sensors` command with json output
"""
class LinuxSensors(TempSensor):
    def get_cpu_temp_command(self) -> str:
        return 'sensors -j'

    def parse_temp_response(self, res: str) -> float:
        temps = json.loads(res)
        keys = temps.keys()

        if len(keys) == 1:
            temps = temps[list(keys)[0]]
        else:
            raise Exception(f'Unexpected format {temps}')

        keys = list(temps.keys())

        temp_sample = []
        for key in keys:
            if 'Core' not in key:
                continue
            measurement = temps[key]
            
            mk = list(measurement.keys())
            for k in mk:
                if 'input' in k:
                    temp_sample.append(measurement[k])        
        
        return sum(temp_sample) / len(temp_sample) if len(temp_sample) > 0 else 0
