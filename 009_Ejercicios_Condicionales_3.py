

# Escribe un script que solicite una calificación al usuario (0 - 100). 
# Si la calificación es mayor o igual a 90, imprime "Excelente", si es mayor 
# o igual a 70 y menor que 90, imprime "Bueno", si es mayor o igual a 50 y 
# menor que 70, imprime "Suficiente", y si es menor que 50, imprime "Insuficiente".

calificacion = float(input("Ingresa tu calificación (0-100): "))
if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Bueno")
elif calificacion >= 50:
    print("Suficiente")
else:
    print("Insuficiente")
