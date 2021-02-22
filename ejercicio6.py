def make_box_list(number, symbol):
    if not isinstance(number,int) or not isinstance(symbol,str):
        return None, "Error"
    space = " " 
    make_box_list = []
    for i in range(number):
        ##si el parametro number es 1 y 2 se agrega normal
        if number <= 2:
            make_box_list.append(symbol * number)
        ##sino se agregara de manera diferente
        else:
            ##las primera fila y la ultima se agrega normalmente
            if i == 0 or i == (number - 1):
                make_box_list.append(symbol * number)
            ##las demas filas
            else:
                make_box_list.append(symbol + (space * (number -2)) + symbol)
    return make_box_list