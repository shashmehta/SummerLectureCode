import Motor
import Gyroscope

#Create an object of the motor
motor = Motor()

#create an object of the gyroscope
gyro = Gyroscope()

#Create variables to store the angles
x = 0
y = 0
z = 0

speed = 50

def Setup():
    #Initialize motor 1
    motor.__init__(1)
    #Initialize motor 2
    motor.__init__(2)
    
    #Initialize gyroscope
    gyro.__init__()

while True:
    
    Setup()
    
    #Get all the angles
    x = gyro.get_angle_x()
    y = gyro.get_angle_y()
    z = gyro.get_angel_z()
    
    if x > 0:
        speed = speed - x
        motor.run_motor(speed, "forward")
    if x < 0:
        speed = speed + x
        motor.run_motor(speed, "backward")