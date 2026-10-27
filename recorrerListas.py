colores = ["rojo", "blanco", "amarillo", "azul", "verde"]
videojugos_venta = ["Zelda Breath of the Wild", "Smash Bros", "Mario Kart", "Minecraft"]

# Recorrer uns lista con un ciclo for
for color in colores:
    print("Color:", color)
    
for elemento in videojugos_venta:
    print("Nombre del videojuego:", elemento)

apellidos = ["ANGULO", "CASTILLO", "CABAS", "FUENTES", "HERNANDEZ"]
"""
apellidos = ["ANGULO", "CASTILLO", "CABAS", "FUENTES", "HERNANDEZ"]
item = ANGULO
    Apellido: ANGULO
item = CASTILLO
    Apellido: CASTILLO 
item = CABAS
    Apellido: CABAS
item = FUENTES
    Apellido: FUENTES
item = HERNANDEZ
    Apellido: HERNANDEZ
"""
for item in apellidos: 
    print("Apellido:", item)

tazaDeMedida = [1.5, 2.5, 3.5, 4.5, 5.5]
"""
dobleTaza = [] 

elemento = 1.5
    doble = 2 * 1.5 = 3.0
    dobleTaza.append(3.0) -> dobleTaza = [3.0]

elemento = 2.5 
    doble = 2 * 2.5 = 5.0
    dobleTaza.append(5.0) -> dobleTaza = [3.0, 5.0]

elemento = 3.5
    doble = 2 * 3.5 = 7.0
    dobleTaza.append(7.0) -> dobleTaza = [3.0, 5.0, 7.0]

elemento = 4.5
    doble = 2 * 4.5 = 9.0
    dobleTaza.append(9.0) -> dobleTaza = [3.0, 5.0, 7.0, 9.0]

elemento = 5.5 
    doble = 2 * 5.5 = 11.0
    dobleTaza.append(11.0) -> dobleTaza = [3.0, 5.0, 7.0, 9.0, 11.0]

Lista de dobles: [3.0, 5.0, 7.0, 9.0, 11.0]
"""
dobleTaza = []
for elemento in tazaDeMedida:
    print("elemento = ", elemento)
    doble = 2 * elemento
    print("     doble = 2 *", elemento, "=", doble)
    dobleTaza.append(doble)
    print("     dobleTaza.append(", doble, ") -> dobleTaza =", dobleTaza, "\n")

print("Lista de dobles:", dobleTaza)



"""
enumerate(colores)

enumerate() permite iterar sobre un iterable, generando índices junto con los elementos

enumerate de colores:  
    -  0     "rojo", 
    -  1     "blanco", 
    -  2     "amarillo", 
    -  3     "azul", 
    -  4     "verde"
"""