def number_multiplies(number, length):
    #comprobamos que los argumentos no sean negativos y que si sean ENTEROS
    if not isinstance(number,int) or not isinstance(length,int):
        return None, "Error"
    if number < 0 or length < 0:
        return None, "Error"
    list_of_multiplies = []
    for element in range(1,length + 1):
        list_of_multiplies.append(number * element)
    return list_of_multiplies
