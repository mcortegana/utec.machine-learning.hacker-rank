# Dada la función f(x)=20x-23, construir un programa que reciba
# ingresar un valor para "x" y devuelva el resultado de la función.

variable = input()

if variable.isdigit() and int(variable) >= 0:
    x = int(variable)
    result = 20 * x - 23
    print(result)
