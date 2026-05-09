class person(object):
    def __init__(self,name,Idnumber):
        self.name=name
        self.Idnumber=Idnumber
    def display(self):
        print("The employees name is ",self.name)
        print("The employees Id number is ",self.Idnumber)
class employee(person):
    def __init__(self,name,Idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,Idnumber)
a=employee("Rahul",16512,100000,"Intern")
a.display()
    