
from MorseAlphabet import * 
from MorseLibrary import *

class MainMorse:


    def __init__(self):
        self.alphabet = MorseAlphabet()
        self.lib = MorseLibrary()
        #self.finalMorse = ""

    # need to add the actual blinkit commands
    # and replace the print statements
    def blinkitMorse(self,morseString):
        for x in range(len(morseString)):
            if (morseString[x] == "."):
                try:
                    self.lib.dot()
                except:    
                    print("dot")
                # 
            elif (morseString[x] == "-"):
                try:
                    self.lib.dot()
                except: 
                    print("dash")
                #
            else:
                try:
                    self.lib.space()
                except:
                    print("space")
                #


    def conversion(self, word):
        finalMorse = ""
        for x in range(len(word)):
            finalMorse = finalMorse + self.alphabet.letterToMorse(word[x]) + " "
    
        self.blinkitMorse(finalMorse)
        print(finalMorse)
