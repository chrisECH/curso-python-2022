

numero = [1,2,3,4,5,6,7,8,9,10]

def par(numero):
    if(numero % 2==0):
        return True
    else:
        return False


result = filter(par, numero)

pares = list(result)

print(pares)