class vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        self.capacity=capacity
    def fare(self):
        return self.capacity*100
class bus(vehicle):
    def fare(self):
        bus_fare=super().fare()
        maintenence_charge=bus_fare*0.1
        print("The total bus fare is", bus_fare+maintenence_charge)
school_bus=bus("school bus", 80, 12, 50)
school_bus.fare()