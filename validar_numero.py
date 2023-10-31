def validar_numero(cadena):
    # Borra la instrucción pass y escribe aquí tu código
    digitos = ["0","1","2","3","4","5","6","7","8","9","0"]
    signo = ["+","-"]
    if cadena[0] in signo:
        cadena_limpia = cadena[1:]
    elif cadena [-1] in signo:
        cadena_limpia = cadena[:-1]
    else:
        cadena_limpia = cadena
    puntos = []
    resultado =[]
    for caracter in cadena_limpia:
        if caracter == ".":
            puntos.append(1)
        elif caracter in digitos:
            numero = True
        else:
            numero = False
        resultado.append(numero)
    if False in resultado or len(puntos) > 1:
        respuesta = "no valido"
    else:
        respuesta = "válido"
    return respuesta
# Escribe aquí código para probar la función
cadena = input("Introduzca el texto a verificar: ")
print(validar_numero(cadena))
