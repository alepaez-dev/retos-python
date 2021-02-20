def format_number(number, separator):
    if not isinstance(number,int) or not isinstance(separator,str):
        return None, "Error"
    if number < 0:
        return None, "Error"
    string_number = str(number)
    list_positions = []
    length_string = len(string_number)
    stop_count = 0
    new_string = ""
    #agregamos las posiciones donde se pone el separator en un arreglo
    for index in range(length_string):
        stop_count += 1
        if stop_count == 3:
            list_positions.append(index)
            stop_count = 0
    print(list_positions)
    #iteramos con la longitud del string dado para ir agregando caracter por caracter
    for index_string in range(length_string):
        #iteramos con la lista de las posiciones donde se agrega el separados
        for position in list_positions:
            if index_string == position:
                new_string += separator
        new_string += string_number[index_string]
    print(new_string)
        




    
    