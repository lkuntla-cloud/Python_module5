class myclass:
    __privVar=27
    
    def __privmethod(self):
        print("This is a private method")
    def hello(self):
        print("The private variable value is: ",myclass.__privVar)
foo=myclass()
foo.hello()
foo.__privmethod()
