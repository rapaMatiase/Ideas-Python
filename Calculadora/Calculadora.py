import tkinter as tk

operaciones = {
    "+" : lambda a,b : a + b,
    "-" : lambda a,b : a - b,
    "*" : lambda a,b : a * b,
    "/" : lambda a,b : a / b
}

def operar(a, b, operacion):
    resultadoDeLaOperacion = operaciones[operacion](a, b)
    return resultadoDeLaOperacion

def acumularOperacion():
    seguirAcumulando = input("Mantener valor?(y/n)")
    acumular = True
    if("n" == seguirAcumulando):
        acumular = False
    return acumular

def inputOperacion():
    operaciones = ["+","-","*","/"]
    operacionIngresada = input("Ingrese una operacion (+ - * /)")
    IngresoEsValido = operacionIngresada in operaciones
    while not IngresoEsValido:
        print("El valor ingresado no es valido!!")
        operacionIngresada = input("Ingrese una operacion (+ - * /)")
        IngresoEsValido = operacionIngresada in operaciones
    return operacionIngresada

def inputNumber():
    numeroIngresado = input("Ingrese un numero")
    numeroConvertido = int(numeroIngresado)
    return numeroConvertido 

if __name__ == '__main__':
    utilizarResultadoDeLaOperacionAnterior = False
    resultado = 0

    while(True):

        if not utilizarResultadoDeLaOperacionAnterior:
            a = inputNumber()
            utilizarResultadoDeLaOperacionAnterior = True
        else:
            a = resultadoDeLaOperacion
        
        operacionIngresada = inputOperacion()
        b = inputNumber()

        resultadoDeLaOperacion = operar(a, b, operacionIngresada)
        print(resultadoDeLaOperacion)

        utilizarResultadoDeLaOperacionAnterior = acumularOperacion()


