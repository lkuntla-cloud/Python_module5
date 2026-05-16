class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+'('+self.meaning
flash=[]
print("welcome to flashcards application")
while(True):
    word=input("Enter the word: ")
    meaning=input("Enter the meaning of the word: ")
    flash.append(flashcards(word,meaning))
    option=int(input("If you want to continue enter 0 else enter 1: "))
    if option==1:
        break
print(flashcards)
for i in flash:
    print("<",i)