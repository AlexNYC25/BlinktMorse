
from MorseAlphabet import * 
##from MorseLibrary import *

class MainMorse:


    def __init__(self):
        self.alphabet = MorseAlphabet()
        ##self.lib = MorseLibrary()
        #self.finalMorse = ""

    # need to add the actual blinkit commands
    # and replace the print statements
    def blinkitMorse(self,morseString):
        for x in range(len(morseString)):
            if (morseString[x] == "."):
                print("dot")
                # 
            elif (morseString[x] == "-"):
                print("dash")
                #
            else:
                print("space")
                #


    def conversion(self, word):
        finalMorse = ""
        for x in range(len(word)):
            finalMorse = finalMorse + self.alphabet.letterToMorse(word[x]) + " "
    
        print(finalMorse)