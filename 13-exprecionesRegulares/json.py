import json

producto1 = {"nombre":"carro", "color": "gris", "precio":40000}

estructuraJson = json.dumps(producto1)

print(producto1["nombre"])