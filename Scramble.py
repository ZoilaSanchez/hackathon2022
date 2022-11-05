def scramble(word1, word2):
    array1 = getArray(word1)
    array2 = getArray(word2)
    bandera = True
    for index, letter in enumerate(array1):
        if(letter != array2[index]):
            bandera = False
            break
        # print(index, letter)
    return bandera
def getArray(word):
    collection = []
    for letter in word:
        collection.append(letter.lower())
        # print(letter)
    collection.sort()
    return collection
print(scramble("Deudora", "Eduardo"))
print(scramble("ale", "otro"))