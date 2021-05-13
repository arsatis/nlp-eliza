import re

class CommandParser:

    @staticmethod
    def checkIfExit(userInput):
        # TODO: check if there is any way to simplify this into a single line
        if (re.search('(^|[^A-Za-z])(bye|goodbye|exit)', userInput)):
            return True
        else:
            return False