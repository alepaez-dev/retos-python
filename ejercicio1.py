#Crea una funcion que reciba un numero como argumento y devuelva el largo de este numero
def number_length(number):
    #comprobamos que no sea negativo y que si sea ENTERO
    if not isinstance(number,int):
        return None, "Error"
    if number < 0:
        return None, "Error"
    number_string = str(number) ##convertimos a string
    count = 0 #contador
    for character in number_string:
        count += 1; #sumamos 1 al contador por cada caracter del string
    return count;
