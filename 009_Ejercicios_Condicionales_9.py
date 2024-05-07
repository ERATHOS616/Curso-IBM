

# Programa un sistema que categorice los ingresos anuales de una persona 
# como 'bajo', 'medio' o 'alto'. Define tú mismo los límites de cada categoría.

ingresos = float(input("Introduce tus ingresos anuales: "))
if ingresos < 20000:
    print("Tus ingresos son bajos.")
else:
    if ingresos < 50000:
        print("Tus ingresos son medios.")
    else:
        print("Tus ingresos son altos.")
