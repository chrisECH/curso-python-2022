def positivo(numero):
    if numero > 0:
        return True
    else:
        return False

numero = [4, -2, 8, -3, -5, -7, 1, 9]

filtro = filter(positivo, numero)

result = list(filtro)

print (result)