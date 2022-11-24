def operacion(x1, x2, x3):
    result = x1 / (x2 - x3)
    return result


try:
    print(operacion(6,3,3))
except:
    print("Ha habido un error en la operacion")