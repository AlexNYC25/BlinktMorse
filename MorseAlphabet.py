

class MorseAlphabet:

    def __init__(self):
        print("Alphabet set up")


    def letterToMorse(self, letter):
        if letter.upper() == "A":
            return ".-"
        elif letter.upper() == "B":
            return  "-..."
        elif letter.upper() == "C":
            return "-.-."
        elif letter.upper() == "D":
            return "-.."
        elif letter.upper() == "E":
            return "."
        elif letter.upper() == "F":
            return  "..-."
        elif letter.upper() == "G":
            return  "--."
        elif letter.upper() == "H":
            return "...."
        elif letter.upper() == "I":
            return ".."
        elif letter.upper() == "J":
            return ".---"
        elif letter.upper() == "K":
            return "-.-"
        elif letter.upper() == "L":
            return ".-.."
        elif letter.upper() == "M":
            return "--"
        elif letter.upper() == "N":
            return "-."
        elif letter.upper() == "O":
            return "---"
        elif letter.upper() == "P":
            return ".--."
        elif letter.upper() == "Q":
            return "--.-"
        elif letter.upper() == "R":
            return ".-."
        elif letter.upper() == "S":
            return "..."
        elif letter.upper() == "T":
            return "-"
        elif letter.upper() == "U":
            return "..-"
        elif letter.upper() == "V":
            return "...-"
        elif letter.upper() == "W":
            return ".--"
        elif letter.upper() == "X":
            return "-..-"
        elif letter.upper() == "Y":
            return "-.--"
        elif letter.upper() == "Z":
            return "--.."
        elif letter == "1":
            return ".----"
        elif letter == "2":
            return "..---"
        elif letter == "3":
            return "...--"
        elif letter == "4":
            return "....-"
        elif letter == "5":
            return "....."
        elif letter == "6":
            return "-...."
        elif letter == "7":
            return "--..."
        elif letter == "8":
            return "---.."
        elif letter == "9":
            return "----."
        elif letter == "0":
            return "-----"
        else:
            return " "










