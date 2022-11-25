numero = [1,2,3,4,5,6,7,8,9,10]

def incremento(numero):
    return numero + 10

result = map(incremento, numero)

sumatoria = list(result)

print(sumatoria)