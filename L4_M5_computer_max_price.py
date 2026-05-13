class computer:
    def __init__(self):
        self.__max_price=900
    def sell(self):
        print("The selling price is: ",self.__max_price)
        
    def setMax_price(self,price):
        self.__max_price=price
C=computer()
C.sell()
C.__max_price=1000
C.sell()
C.setMax_price(1000)
C.sell()