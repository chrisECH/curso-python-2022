

def multiplicar(numero):
    return numero * 2

numeros = [2, 4, 6]

mapeo = map(multiplicar, numeros)

result = list(mapeo)

print(result)

listar_resultado = list(map(multiplicar, numeros))

print(listar_resultado)

listar_resultado2 = list(map(lambda numero: numero * 2, numeros))

print(listar_resultado2)