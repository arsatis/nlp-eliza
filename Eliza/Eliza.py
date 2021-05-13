import re

class Eliza:
    def __init__(self):
        self.name = "Eliza"
        print("Hello! I'm " + self.name + ". How can I help you today?")

    def parse(self, userInput):
        print("hello!")

# user commands
eliza = Eliza()
userInput = input().lower()

while not (re.search("[^A-Za-z]?bye", userInput) 
        or re.search("exit", userInput)):
    eliza.parse(input)
    userInput = input().lower()
else:
    print("bye!")