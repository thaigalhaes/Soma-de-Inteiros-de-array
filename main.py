def validar_array(array):
    for posicao,numero in enumerate(array):
        proxima_posicao = posicao + 1
        while( proxima_posicao  < len(array)):
            if numero + array[proxima_posicao] == 42:
                return True
            else:
                proxima_posicao += 1
        return validar_array(array[1:])
    return False

array = input ("Digite seus numeros:").split(",")
array = [int(x) for x in array]
print ("O valor é:{}".format(validar_array (array)))