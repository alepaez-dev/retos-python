def number_multiplies(number, length):
    #si los argumentos NO SON ENTEROS
    if not isinstance(number,int) or not isinstance(length,int):
        return None, "Error"
    #si los argumentos SON NEGATIVOS
    if number < 0 or length < 0:
        return None, "Error"
    list_of_multiplies = [number * element for element in range(1, length + 1)]
    return list_of_multiplies
  
