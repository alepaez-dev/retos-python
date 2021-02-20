#Crea una funcion que reciba un numero como argumento y devuelva el largo de este numero
def number_length(number):
    #comprobamos que no sea negativo
    if isinstance(number,int) and number > 0:
        number_string = str(number) ##convertimos a string
        count = 0 #contador
    else:
        return None, "Error"
    for character in number_string:
        count += 1; #sumamos 1 al contador por cada caracter del string
    return count;
