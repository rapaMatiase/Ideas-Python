# PASO 3.2 - IMPRIMIENDO EN PANTALLA EL TABLERO DE JUEGO

# Necesitamos mostrar el tablero de juego en pantalla para que el usuario comienza a tomar deciciones
# de como completar el mismo.

sodokuDesboard = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# Planteo para 3.1
# Si hacemos un print simplemente el problema es que el resultado sera el siguiente. 
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Lo que no es lo mas amigable para el usuario, porque un renglon y no una tabla.
# CODIGO
print(sodokuDesboard)
