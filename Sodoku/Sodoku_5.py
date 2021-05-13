# PASO 3.2 - IMPRIMIENDO EN PANTALLA EL TABLERO DE JUEGO

sodokuDesboard = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

numberOfRows = len(sodokuDesboard)
for i in range(0, numberOfRows):
    print(sodokuDesboard[i])

#Solicito la fila donde quiere insertar
numberRow = input("Ingrese la fila donde desea jugar : ")
#Convertimos el ingreso a valor numerico
numberRow = int(numberRow)

#Solicito la fila donde quiere insertar
numberColoum = input("Ingrese la columna donde desea jugar : ")
#Convertimos el ingreso a valor numerico
numberColoum = int(numberColoum)

# 

print(sodokuDesboard[numberOfRows][numberColoum])
