from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self,x):
        print("The given value is: ",x)
    @abstractmethod
    def task(self):
        print("We are in abstract task")
class test_class(absclass):
    def task(self):
        print("We are in test_class task")
test_obj=test_class()
test_obj.task()
test_obj.print(100)