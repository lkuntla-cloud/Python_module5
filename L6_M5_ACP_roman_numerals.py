class roman_numerals:
    def roman_numerals(self,num:int):
        roman_numerals_dict={1000:"M",900:"CM",500:"D", 400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        roman_numerals=""
        for value, numerals in roman_numerals_dict.items():
            while num>=value:
                roman_numerals+=numerals
                num-=value
        return roman_numerals
user_input=int(input("Enter an integer to convert into roman numerals: "))
converter=roman_numerals()
result=converter.roman_numerals(user_input)
print("The roman numerals of {} are {}".format(user_input,result))
