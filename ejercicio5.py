#encontrar repeticiones
lista = ["perro", "gato", "perro", "color", "perro", "gato","pera","gato","manzana"]
def change_duplicates(lista):
    #validacion que sea lista
    if not isinstance(lista, list):
        return None, "Error"
    #validacion que todos los elementos sean stirng
    for element in lista:
        if not isinstance(element,str):
            return None, "Error, los elementos no son todos String"
    lista_copy = lista.copy()
    new_list = []
    index_1 = 0
    #lo hacemos con indice
    while index_1 < len(lista_copy):
        repetition_found = False
        #index_next siempre es uno despues para no repetir todo el ciclo
        index_next = index_1 + 1 
        while index_next < len(lista_copy):
            if lista_copy[index_1] == lista_copy[index_next]:
                #eliminamos repeticiones de la lista_copy
                lista_copy.pop(index_next)
                #damos por encontrada repeticion
                repetition_found = True
                #hacemos la palabra prulal
                plural_word = lista_copy[index_1] + "s"
                #la agregamos a la nueva lista_copy SOLO SI NO ESTA
                if plural_word not in new_list:
                    new_list.append(plural_word)
            index_next += 1
            #si no hubo ninguna repeticion, agregamos la palabra asi nada mas
        if repetition_found == False:
            new_list.append(lista_copy[index_1])
        index_1 += 1
    return new_list
