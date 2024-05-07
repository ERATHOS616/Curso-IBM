

# Una tienda ofrece descuentos basados en el total de compra. 
# Si la compra es mayor a $100, el descuento es del 10%. Si es mayor a $500, 
# el descuento es del 20%. Crea un programa que calcule el total a pagar 
# después del descuento.

compra = float(input("Introduce el total de la compra: $"))
if compra > 500:
    total = compra * 0.8
    print(f"El total después del descuento es: ${total:.2f}")
else:
    if compra > 100:
        total = compra * 0.9
        print(f"El total después del descuento es: ${total:.2f}")
    else:
        print(f"No hay descuento. El total es: ${compra:.2f}")
