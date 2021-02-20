#normal
def factorial(number):
    total = 1 #si es 1 factorial es 1
    while number > 1:
        total *= number
        number -= 1 #restamos el numero
    return total