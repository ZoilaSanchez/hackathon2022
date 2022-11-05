
print(" ---------------- ")
print(" Abuela binaria")
print(" ---------------- ")
N = input('Ingrese total = ')
num1= input('Ingrese primer numero = ')
num2= input('Ingrese segundo numero = ')
total= int(num1)+int(num2)
if( total == int(N)):
    bin = format(int(num1), "b")
    bin2 = format(int(num2), "b")
    suma = bin.count("1")+ bin2.count("1")
    print("\n*************** ")
    print("Resultados:")
    print("Total es {} \nEl numero 1 es : {} \nEl numero 2 es: {}\n*********************************************** \n  La cantidad de avellanas es de : {} \n***********************************************".format(N, num1,num2,suma))
else:
    print("***********************************************\nLos numero {} , {} no son iguales a {}".format(num1,num2,N))


