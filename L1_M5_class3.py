class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
BLU=Parrot("blu",10)
WOO=Parrot("WOO", 15)

print("{} is a {}".format(BLU.name,BLU.species))
print("{} is a {}".format(WOO.name,WOO.species))

print("{} is {} years old".format(BLU.name,BLU.age))
print("{} is {} years old".format(WOO.name,WOO.age))