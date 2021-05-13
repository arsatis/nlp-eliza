from commands.CommandParser import *
import re
import random

class Eliza:
    def __init__(self):
        self.name = 'Eliza'
        print("Hello! I'm " + self.name + '. How can I help you today?')

    def respond(self, userInput):
        greetings = {'hi!', 'hello!', 'hey!', 'heyo!', 'sup!', 'yo!'}
        print(random.sample(greetings, 1)[0] + '\n')

# initialize Eliza
eliza = Eliza()

# user commands
userInput = input().lower()
while not (CommandParser.checkIfExit(userInput)):
    eliza.respond(input)
    userInput = input().lower()
else:
    print('bye!')