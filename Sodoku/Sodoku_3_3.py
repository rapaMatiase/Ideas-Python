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
# CODIGO
# print(sodokuDesboard[0])
# print(sodokuDesboard[1])
# print(sodokuDesboard[2])

# PROPUESTA 3.3
# El codigo anterior funciona paero tiene un problema. Si la matrix
# se le quita o agregan filas, ya no sirve. En pocas palabras, el 
# codigo anterior no es escalable. Una solucion sencialla y escalable,
# seria utiliza un for para recorrer el array que contiene cada fila.

# La funcion len nos permite saber la cantidad de elementos que 
# tiene un array. En este caso nos dice la cantidad de filas
# de la matrix, en este caso un 3.
numberOfRows = len(sodokuDesboard)
# La i toma los valores entre 0 hasta el numberOfRows sin incluir.
# La i toma los valores entre 0 y 2, no llega al 3.
for i in range(0, numberOfRows):
    print(sodokuDesboard[i])

# Probablemente te estas preguntando si esto es valido, y si lo es.
# for i in range(0, len(sodokuDesboard)):
#     print(sodokuDesboard[i])
