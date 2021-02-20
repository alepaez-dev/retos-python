def format_number(number, separator):
    if not isinstance(number,int) or not isinstance(separator,str):
        return None, "Error"
    if number < 0:
        return None, "Error"
    string_number = str(number)
    new_string = ""
    stop_count = 0
    index = len(string_number) - 1
    #iteramos desde el final hasta el principio
    while index >= 0 :
        stop_count += 1
        #cada 3 posiciones agregar el separator
        if stop_count == 4:
            new_string += separator
            stop_count = 0
        #sino simplemente agregar el caracter que es
        else:
            new_string += string_number[index]
            index -=1
    #le damos reverse
    new_string = new_string[::-1]
    print(new_string)
    return new_string





    
    