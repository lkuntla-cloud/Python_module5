class reverse:
    def __init__(self, s):
        self.s=s
    def reverse_string(self):
        words=self.s.split()
        reversed_words=[word[::-1]for word in words]
        print("The reversed string is: "," ".join(reversed_words))
s_input=input("Enter the string you want to reverse: ")
reversed_string=reverse(s_input)
reversed_string.reverse_string()