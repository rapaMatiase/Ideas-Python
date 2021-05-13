# Analizamos el juego antes de arrancar a programar.

# TABLERO DE JUEGO
# Un tablero de nueve filas por nueve columnas, y esta divididas en nueve sectores de 
# tres por tres. Las celdas toman valores entre el intervalo de 1 y 9. Algunas de las 
# celdas tiene valores numericos fijos como parte del juego para agregar cierto grado 
# de dificultad. 

# CANTIDAD DE JUGADORES : 1

# FLUJO DEL JUEGO
# El jugador debe completar las celdas con valores entre 1 a 9 considerando los valores fijos
# en el tablero y los completados anteriormente para evitar repetidos en filas, columnas y
# sectores.

# REGLAS DE JUEGO
# Ninguna en particular.

# ¿CUANDO SE GANA?
# Cuando todas las filas y columnas estan completas, sin numeros repetidos en ninguna 
# fila, columna y sector. 

# ¿CUANDO SE PIERDE?
# No se pierde, simplemente se cambian los valores de las celdas hasta lograr la solucionarlo.

# SIMPLIFICANDO EL PROBLEMA
# La dinamica del juego no es muy complicada en si, pero afectos de nuestro objetivo educativo
# simplificaremos un poco lo descripto anteriormente. 
# - Un tablero 3x3, no de 9x9 entonces el intervalo de valores de la celda sera de 1 a 3.
# - Al tener un tablero chico no habra sectores, por lo que el juego se gana cuendo
# no haya repetidos en filas y columnas. 