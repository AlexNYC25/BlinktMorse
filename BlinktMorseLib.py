
from MorseAlphabet import * 
from MorseLibrary import *

class BlinktMorseLib:


    def __init__(self):
        self.alphabet = MorseAlphabet()
        self.lib = MorseLibrary()

    def wordConversion(self, word):
        finalMorse = ""
        for x in range(len(word)):
            finalMorse = finalMorse + self.alphabet.letterToMorse(word[x]) + " "
    
        self.blinkitMorse(finalMorse)
        print(finalMorse)

    def blinkitMorse(self,morseString):
        for x in range(len(morseString)):
            if (morseString[x] == "."):
                try:
                    self.lib.dot()
                except:    
                    print("dot")
                finally:
                    time.sleep(3)
            elif (morseString[x] == "-"):
                try:
                    self.lib.dot()
                except: 
                    print("dash")
                finally:
                    time.sleep(3)
            else:
                try:
                    self.lib.space()
                except:
                    print("space")
                finally:
                    time.sleep(3)




