class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class Bus(vehicle):
    pass
obj=Bus("volvo bus",180,19)
print("name of bus is: ", obj.name,"max_speed = ", obj.max_speed," mileage is: ",obj.mileage)