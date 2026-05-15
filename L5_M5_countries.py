from abc import ABC, abstractmethod
class India():
    def capital(self):
        print("The capital of India is New Dehli")
    def language(self):
        print("India has many langueages but most spoken language is hindi")
    def development(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("The capital of USA is Washington DC")
    def language(self):
        print("In the USA english is the most spoken language")
    def development(self):
        print("USA is a developed country")
obj_ind=India()
obj_USA=USA()
for country in(obj_ind,obj_USA):
    country.capital()
    country.language()
    country.development()