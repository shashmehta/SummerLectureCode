class Motor:
    
    MotorPower = 50
    
    def __init__(self, motor_id):
        
        self.motor_id = motor_id
        print("Intializing Motor" + self.motor_id)
    
    def run_motor(self, speed, direction):
        
        if direction == "forward":
            motorPower = speed
            
        if direction == "backward":
            motorPower = -speed