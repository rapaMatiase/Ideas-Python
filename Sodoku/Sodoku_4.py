# PASO 3.2 - IMPRIMIENDO EN PANTALLA EL TABLERO DE JUEGO

sodokuDesboard = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

numberOfRows = len(sodokuDesboard)
for i in range(0, numberOfRows):
    print(sodokuDesboard[i])

# Ahora necesitamos solicitar la posicion donde el jugador
# desea colocar un numero, para comenzar a jugar.

#Solicito la fila donde quiere insertar
numberRow = input("Ingrese la fila donde desea jugar : ")
# La funcion STRING convierte el ingreso del usaurio en string
# nosotros necesitamso convertirlo en valor numerico, y lo
# lo podemos hacer usando la funcion INT.
numberRow = int(numberRow)
#Esta linea se lee como; convertimos el valor string en numberRow
# en int y lo guardamos en la misma variable. Es una expresion
# recursiva.

#Repito los dos pasos de arriba para solicitar la columna
numberColoum = input("Ingrese la columna donde desea jugar : ")
numberColoum = int(numberColoum)

# Todavia no vamos a intentar cambiar el valor de la posicion
# en la matrix. Solo imprmir por consola el valor de la posicion
# ingresada por el usuario.

# Intente ingresar para la fila posicion 3 y para la columna
# posicion 3. 

# Esta linea se lee como 
# sodokuDesboard[N° FILA][N° COLUMNA]
print(sodokuDesboard[numberOfRows][numberColoum])

# Si ingresas 3 y 3 te tiro el siguiente error
# IndexError: list index out of range

# Eso ocurre porque en programacion la primera posicion no es la 1,
# si no la 0, y la ultima posicion no es la 3, si no la 2. Vuelve a 
# ejecutar el programa e ingresa 2 y 2, el error no volvera a ocurrir.
# Por ahora supondremos que el usuario siempre ingresa valores validos.