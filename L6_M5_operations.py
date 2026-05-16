class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if (self.a<other.a):
            print("ob1 is greater than ob2")    
        else:
            print("ob1 is greater than ob2")   
            
    def __eq__(self, other):
        if (self.a==other.a):
           print("object are equal") 
        else:
            print("the objects are not equal")
ob1=A(1)
ob2=A(2)
print("The values are: ",ob1.a,ob2.a)
print(ob1<ob2)

ob3=A(4)
ob4=A(4)
print("The values are: ",ob3.a,ob4.a)
print(ob1==ob2)