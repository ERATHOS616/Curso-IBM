




# Escribe un script que solicite al usuario su edad y asegúrate de que el 
# número proporcionado esté entre 1 y 100. Si el número está fuera de ese rango, 
# pídele que lo introduzca nuevamente.

edad = int(input("Introduce tu edad (entre 1 y 100): "))
while edad < 1 or edad > 100:
    print("Error: la edad debe estar entre 1 y 100.")
    edad = int(input("Introduce tu edad nuevamente: "))
print("Edad válida introducida:", edad)



