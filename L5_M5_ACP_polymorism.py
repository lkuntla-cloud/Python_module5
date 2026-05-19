class BMW:
    def fuel_type(self):
        print("BMW fuel type: Diesel")

    def max_speed(self):
        print("BMW max speed: 240 km/h")


class Ferrari:
    def fuel_type(self):
        print("Ferrari fuel type: Petrol")

    def max_speed(self):
        print("Ferrari max speed: 340 km/h")

obj_bmw=BMW()
obj_ferrari=Ferrari()
for cars in (obj_bmw,obj_ferrari):
    cars.fuel_type()
    cars.max_speed()