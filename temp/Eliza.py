import random

from eliza.commands.CommandParser import CommandParser

class Eliza:
    __name = 'Eliza'
    __inputHeader = 'You: '
    __responseHeader = __name + ': '

    def __init__(self):
        print(self.__responseHeader + "Hello! I'm " + self.__name + '. How can I help you today?')

    def respond(self, userInput):
        # TODO: modify this temporary response
        greetings = {'hi!', 'hello!', 'hey!', 'heyo!', 'sup!', 'yo!'}
        print(self.__name + ': ' + random.sample(greetings, 1)[0] + '\n')

    def run(self):
        userInput = input(self.__inputHeader).lower()
        while not (CommandParser.checkIfExit(userInput)):
            self.respond(input)
            userInput = input(self.__inputHeader).lower()
        else:
            print(self.__name + ': bye!')