from eliza.controller.PorterStemmer import PorterStemmer
from eliza.controller.commands.CommandParser import CommandParser

class Eliza:
    __name = 'Eliza'
    __responsePrefix = __name + ': '
    __inputPrefix = 'You: '

    def __init__(self):
        print(self.__responsePrefix + "Hello! I'm " + self.__name + '. How can I help you today?')

    def respond(self, userInput):
        ps = PorterStemmer()
        arr = []
        for token in userInput.split():
            arr += [ps.stem(token)]
        userInput = ' '.join(map(str, arr)) # user input as a string, after stemming
        print(self.__responsePrefix + CommandParser.parse(userInput))
        # 

    def run(self):
        userInput = input(self.__inputPrefix).lower()
        while not (CommandParser.checkIfExit(userInput)):
            self.respond(userInput)
            userInput = input(self.__inputPrefix).lower()
        else:
            print(self.__responsePrefix + 'bye!')