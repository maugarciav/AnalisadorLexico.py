
estados_aceptacion = {1, 2, 3, 4,5, 6, 7,8,}

def lexerAritmetico(palabra):
    

    d = [{"=" : 1, "+" : 2, "-" : 3, "*" : 4, "/" : 5, "^" : 6, "(" : 7, ")" : 8}]

    estado = 0
    for simbolo in palabra:
        estado = d[estado][simbolo]
        if estado in estados_aceptacion:
            break


    if estado == 1: print("Asignacion"), 
    elif estado == 2: print ("Suma")
    elif estado == 3: print ("Resta")
    elif estado == 4: print ("Multiplicacion")
    elif estado == 5: print ("Division")
    elif estado == 6: print ("Potenica")
    elif estado == 7: print ("Paréntesis que abre")
    elif estado == 8: print ("Paréntesis que cierra")
    else: print("No se reconocio el token")

    

   

with open ("example.txt") as file:
    for line in file:
        lexerAritmetico(line)