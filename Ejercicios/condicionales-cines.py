"""
Un cine desea calcular el precio que debe pagar un cliente por sus entradas. El precio normal de cada entrada es de ₡3 500.

El programa debe solicitar:

Edad del cliente.
Cantidad de entradas.
Utilice las siguientes reglas:

Las personas menores de 12 años reciben un 20 % de descuento.
Las personas de 65 años o más reciben un 15 % de descuento.
Las demás personas pagan el precio normal.
Si el cliente compra 4 entradas o más, recibe 1 bebida gratis.
"""
# Constantes
PRECIO_ENTRADA = 3500
DESCUENTO_MENOR = 0.20
DESCUENTO_ADULTO_MAYOR = 0.15

# Datos
edad = int(input("Ingrese la edad del cliente: "))
cantidad = int(input("Ingrese la cantidad de entradas: "))

# Precio normal
subtotal = PRECIO_ENTRADA * cantidad

# Descuentos según edad
if edad < 12:
    descuento = subtotal * DESCUENTO_MENOR
elif edad >= 65:
    descuento = subtotal * DESCUENTO_ADULTO_MAYOR
else:
    descuento = 0

# Precio final
total = subtotal - descuento

# Bebida gratis
if cantidad >= 4:
    print("Recibe 1 bebida gratis.")

print("Subtotal: ₡", subtotal)
print("Descuento: ₡", descuento)
print("Total a pagar: ₡", total)