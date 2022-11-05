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

print(" ---------------- ")
print(" Scramble ")
print(" ---------------- ")
nomb1 = input(' Ingrese Cadena 1 = ')
nomb2= input(' Ingrese Cadena 2 = ')

if(len(nomb1)== len(nomb2)):
    print("\n*************** ")
    print("Resultados:")
    print("¿La cadena {} es cadena desordenada de {}? = {}".format(nomb2,nomb1,scramble(nomb1, nomb2)))
else:
    print("\n*************** ")
    print("Resultados:")
    print("¿La cadena {} es cadena desordenada de {}? = {}".format(nomb2,nomb1,False))