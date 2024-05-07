


# Crea un programa que sume números introducidos por el usuario hasta que el 
# usuario introduzca 0. Al final, el programa debe mostrar la suma total.

suma = 0
numero = int(input("Introduce un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Introduce otro número (0 para terminar): "))
print("La suma total es:", suma)





