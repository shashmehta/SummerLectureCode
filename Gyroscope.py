class Gyroscope:
    
    #Create a class variable to store the angle along the axis
    angle_x = 0
    angle_y = 0
    angle_z = 0
    
    def __init__(self):
        
        # Initialize gyroscope here
        print("Initializing Gyroscope")

    def get_angle_x(self):
        
        # Retrieve angle along the x-axis
        print("Getting angle along x-axis")
        angle_x = 10
        return angle_x
    
    def get_angle_y(self):
        
        # Retrieve angle along the y-axis
        print("Getting angle along y-axis")
        angle_y = 0
        return angle_y

    def get_angle_z(self):
        
        # Retrieve angle along the z-axis
        print("Getting angle along z-axis")
        angle_z = 0
        return angle_z