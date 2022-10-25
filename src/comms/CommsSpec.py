"""
Spec for implementation of communication channels for set points and feedback
"""
class CommsSpec:
    
    """
    Set the model fanspeed
    pwm: int pwm speed, must be a value between 0 and 100

    returns true if updated, false otherwise
    """
    def set_fanspeed(self, pwm: int) -> bool:
        pass 

    """
    Get model temperature
    returns the model temp in celcius
    """
    def get_temp_c(self) -> float:
        pass