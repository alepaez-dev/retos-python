#normal
def factorial(number):
    total = 1 #si es 1 factorial es 1
    #multiplicamos desde el numero hasta llegar a 2
    while number > 1:
        total *= number
        number -= 1 #restamos el numero para interactuar con todos
    return total

##recursividad
def factorial_recursividad(number):
    #nuestro stop sera cuando llegue a 1
    if number > 1:
        #multiplicamos el numero por el resultado de la misma funcion con un numero antes
        #example: 7 * (6 * (5 * (4 * (3 * (2 * )))) )
        return number * factorial_recursividad(number - 1)
    else:
        return 1