

# Solicita dos números al usuario y determina cuál de los dos es mayor o si son iguales.

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
if numero1 > numero2:
    print("El primer número es mayor.")
elif numero1 < numero2:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")
