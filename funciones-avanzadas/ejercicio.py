

def primos(maximo):
    for numero in range(maximo):
        if(numero in numeros_primos):
            yield numero
        if(numero > 100):
            break

