"""
Variables: Un espacio en la memoria de la computadora donde se guarda un dato 
Sintaxis: nombreVariable = datoQueAlmacenaLaVariable

Tipos de datos:
    - Números: 12, 12.3, -25, -63.78
    - String: "Alexander", "ABF-222", "12"
    - Booleano: true/falso, verdadero/falso, 1/0
"""
nombreJugador = "Camila"
nombreJugador = "Rose" 
nombreJugador = input("Ingrese su nombre (presione enter para continuar): ")
print("Bienvenido(a)", nombreJugador)

bombilloApagado = False
print("¿Bombillo apagado?", bombilloApagado)

bombilloApagado = True
print("¿Bombillo apagado?", bombilloApagado)

# Conversión de datos 
puntaje = int(input("Ingrese su puntaje: "))
print("Su puntaje más 5 es: ", puntaje + 5)

tipoCambio = float(input("El tipo de cambio del euro: "))
print("El tipo de cambio del euro es: ", tipoCambio + 5)

print()