# PASO 3.2 - IMPRIMIENDO EN PANTALLA EL TABLERO DE JUEGO

# Necesitamos mostrar el tablero de juego en pantalla para que el usuario comienza a tomar deciciones
# de como completar el mismo.

sodokuDesboard = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# PROPUESTA 3.1
# Si hacemos un print simplemente el problema es que el resultado sera el siguiente. 
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Lo que no es lo mas amigable para el usuario, porque un renglon y no una tabla.
# CODIGO
# print(sodokuDesboard)

# PROPUESTA 3.2
# Si deseamos imprimir en pantalla en formato de tabla, podemos simplemente
# imprimir un fila debajo de la otra

print(sodokuDesboard[0])
print(sodokuDesboard[1])
print(sodokuDesboard[2])