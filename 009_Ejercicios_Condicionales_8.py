

# Escribe un programa que sugiera qué ponerse basado en la temperatura actual 
# (en grados Celsius) que el usuario introduce. Considera:

# Menos de 10°C: Abrigo y bufanda.
# De 10°C a 20°C: Suéter ligero.
# Más de 20°C: Camiseta.

temperatura = float(input("¿Cuál es la temperatura actual en grados Celsius? "))
if temperatura < 10:
    print("Deberías usar abrigo y bufanda.")
else:
    if temperatura <= 20:
        print("Un suéter ligero sería adecuado.")
    else:
        print("Es un buen día para llevar camiseta.")
