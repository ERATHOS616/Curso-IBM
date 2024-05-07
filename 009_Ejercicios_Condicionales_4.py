

# Un almacén da un descuento del 15% si la compra del cliente supera los 1000 Euros. 
# Escribe un programa que pida el total de la compra y calcule el descuento 
# (si aplica) y el total a pagar.

# Solicita al usuario que ingrese el total de la compra
total_compra = float(input("Ingresa el total de la compra: $"))

# Verifica si el total de la compra supera los 1000 dólares
if total_compra > 1000:
    # Calcula el descuento
    descuento = total_compra * 0.15
    # Redondea el descuento a dos decimales
    descuento_redondeado = round(descuento, 2)
    # Calcula el total final aplicando el descuento redondeado
    total_final = total_compra - descuento_redondeado
    # Redondea el total final a pagar a dos decimales
    total_final_redondeado = round(total_final, 2)
    # Imprime el total final a pagar y el descuento aplicado
    print(f"Se aplicó un descuento de ${descuento_redondeado}, total a pagar: ${total_final_redondeado}")
else:
    # Si no se aplica descuento, el total a pagar es el mismo que el total de la compra
    # Redondea el total de la compra a dos decimales
    total_compra_redondeado = round(total_compra, 2)
    print(f"No se aplicó descuento, total a pagar: ${total_compra_redondeado}")
