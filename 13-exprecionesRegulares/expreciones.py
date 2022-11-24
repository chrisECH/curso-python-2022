import re

texto = "Hola, mi nombre wes christian"

resultado = re.search("nombre", texto)

if(resultado):
    print("Hubo coincidencias")
else:
    print("No hubo coincidencias")
