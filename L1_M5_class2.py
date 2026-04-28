class vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed=max_speed
        self.mileage=mileage
vehicle1=vehicle(240, 18)
print("The max speed of the vehicle is: ",vehicle1.max_speed)
print("The mileage of the vehicle is: ",vehicle1.mileage)