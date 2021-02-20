#normal
def factorial(number):
    total = 1 #si es 1 factorial es 1
    #multiplicamos desde el numero hasta llegar a 2
    while number > 1:
        total *= number
        number -= 1 #restamos el numero para interactuar con todos
    return total