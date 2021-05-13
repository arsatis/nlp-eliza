import re
import random

class CommandParser:

    @staticmethod
    def checkIfExit(userInput):
        if re.search('(^|[^A-Za-z])(bye|goodbye|exit)', userInput):
            return True
        else:
            return False

    """
    Eliza responds based on Eckman's classification of emotions into 6 categories.
    Visit https://www.verywellmind.com/an-overview-of-the-types-of-emotions-4163976 for details about this classification.

    TODO: to implement ML algorithms to better classify each emotion, rather than hard-coding keywords for each emotion.
    """
    @staticmethod
    def parse(userInput):
        # sad emotions
        if re.search('(^|[^A-Za-z])(agoni|cry|depress|despair|grief|hurt|lonel?i?|sad|sorrow|unhappi)($|[^A-Za-z])', userInput):
            return "Don't be sad... Eliza is here!\n"

        # fear emotions
        elif re.search('(^|[^A-Za-z])(fear|frighte?n?|horrifi|horror|panic|shock|terrifi|terror)($|[^A-Za-z])', userInput):
            return "Don't be afraid... Eliza is here!\n"

        # anxiety (subset of fear) emotions
        elif re.search('(^|[^A-Za-z])(anxieti|anxiou|distress|nervou|uneasi|worri)($|[^A-Za-z])', userInput):
            return "Don't worry... everything will be alright!\n"

        # disgust emotions
        elif re.search('(^|[^A-Za-z])(disgust|eww?)($|[^A-Za-z])', userInput):
            return "Eww...\n"

        # anger emotions
        elif re.search('(^|[^A-Za-z])(anger|angri|annoi|dislik|frustrat|hat[er]|jealou|loath|resent)($|[^A-Za-z])', userInput):
            return "Calm down... don't let your emotions get the better of you.\n"

        # surprise emotions
        elif re.search('(^|[^A-Za-z])(amaz|astonish|surpris)($|[^A-Za-z])', userInput):
            return "Oh my!\n"

        # happy emotions
        elif re.search('(^|[^A-Za-z])(ecstasi|enthusias[mt]|euphori?a?|excit|happi|joi|pleasur|relief|satisfi)($|[^A-Za-z])', userInput):
            return "I'm glad to hear that!\n"

        # no emotional words detected
        else:
            greetings = {'hi!', 'hello!', 'hey!', 'heyo!', 'sup!', 'yo!'}
            return random.sample(greetings, 1)[0] + '\n'