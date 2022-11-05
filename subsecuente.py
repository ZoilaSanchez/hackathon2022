

def subSecuente(cad1,cad2):
    #Estandarizar cadenas
    cad1= cad1.lower()
    cad2= cad2.lower()
    cadenas = ""
    #Validar cadenas por tamaño
    tamCad1 = len(cad1)
    tamCad2 = len(cad2)

    if(tamCad1>tamCad2):
        useCad=cad2
        compCad=cad1
    else:
        useCad=cad1
        compCad=cad2
        
    for id, cadena in enumerate(useCad):
            caracter2 = compCad[id]
            if(caracter2==cadena):
                cadenas+=cadena
    return cadenas


print(" -------------------- ")
print(" Cadena Subsecuente")
print(" -------------------- ")
cad1 = input(' Ingrese Cadena 1 = ')
cad2= input(' Ingrese Cadena 2 = ')

print("\n*************** ")
print("Resultados:")
print("La cadena subsecuente de {} y {} es = * {} *".format(cad1,cad2,subSecuente(cad1,cad2)))






