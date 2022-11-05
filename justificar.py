def justificar(array, maxNumber):
    cadenaFinal = ""
    for index, word in enumerate(array):
        if(index != 0):
            cadenaFinal = cadenaFinal + "\n\"" +  completeString(word, maxNumber, index, array) +"\","
        else:
            cadenaFinal = cadenaFinal + "\"" +  completeString(word, maxNumber, index, array) +"\","
    return cadenaFinal
def completeString(word, maxNumber, index, array):
    if(len(word) != maxNumber):
        if(index == len(array) - 1):
            word = word + addSpaces(maxNumber - len(word))
        if(len(word) < maxNumber):
            wordAddSpaces =  splitWord(word)
            while len(word)< maxNumber:
                wordWithSpaces = []
                for index, wordSplitted in enumerate(wordAddSpaces):
                    if(len(' '.join(wordWithSpaces)) > maxNumber):
                        print("rompio")
                        break
                    if(index != len(wordAddSpaces) - 1 ):
                        wordSplitted = wordSplitted + addSpaces(1)
                    wordWithSpaces.append(wordSplitted)
                word = ' '.join(wordAddSpaces)
                wordAddSpaces = wordWithSpaces
            if(len(word) > maxNumber):
                word = word.replace(" ", "", 1)
    return word
def addSpaces(number):
    spaces = ""
    for i in range(number):
        spaces = spaces + " "
    return spaces
def splitWord(word):
    word = word.split(' ')
    return word
print(justificar(["justificar el", "oo oso es", "e d c dfjl", "escribir algo", "b de veras", "d"], 24))