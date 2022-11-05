def justificar(array, maxNumber):
    cadenaFinal = ""
    for index, word in enumerate(array):
        if(index != 0):
            cadenaFinal = cadenaFinal + "\n\"" +  completeString(word, maxNumber, index, array) +"\","
        else:
            cadenaFinal = cadenaFinal + "\"" +  completeString(word, maxNumber, index, array) +"\","
        # completeString(word, maxNumber)
    return cadenaFinal
def completeString(word, maxNumber, index, array):
    if(len(word) != maxNumber):
        if(index == len(array) - 1):
            word = word + addSpaces(maxNumber - len(word))
        if(len(word) < maxNumber):
            # print("no son del mismo length", word)
            wordAddSpaces =  splitWord(word)
            howManyTimesAddSpaces = len(wordAddSpaces)
            while len(word)< maxNumber:
                wordWithSpaces = []
                for wordSplitted in wordAddSpaces:
                    wordSplitted = wordSplitted + addSpaces(1)
                    wordWithSpaces.append(wordSplitted)
                    # print("******", wordSplitted)
                word = ' '.join(wordAddSpaces)
                wordAddSpaces = wordWithSpaces
                # print(word, len(word))
        # print("no son del mismo length", word)
    return word
def addSpaces(number):
    spaces = ""
    for i in range(number):
        spaces = spaces + " "
    return spaces
def splitWord(word):
    word = word.split(' ')
    return word
print("a"+addSpaces(24)+"b")
print(justificar(["justificar el", "oo oso es ", "e"], 24))