class dog:
    species="canine"
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
DOG1=dog(name="Buddy",breed="german shepard",age=7)
DOG2=dog(name="Rocky",breed="golden retriever",age=6)
print("DOG1 is a {} and is called {} and is {} years old".format(DOG1.breed,DOG1.name,DOG1.age))
print("DOG2 is a {} and is called {} and is {} years old".format(DOG2.breed,DOG2.name,DOG2.age))
print("Both of them belong to the species of ",DOG1.species)