# Funcion
def verificacion_palabra(palabra_secreta, palabra_ingresada):
    # Creamos un lista de letras_verificadas
    letras_verificadas = []
    # Cantidad de letras de la palabra secreta
    cantidad_letras = 5

    # Recorremos la palabra de acuerdo a la posicion
    for posicion in range(cantidad_letras):
        
        # Si la letra de la palabra ingresada esta en su lugar y es igual
        if palabra_secreta[posicion] == palabra_ingresada[posicion]:
            letras_verificadas.append("["+palabra_ingresada[posicion]+"]")

        # Sino, si la letra existe pero no esta en su lugar
        elif palabra_ingresada[posicion] in palabra_secreta:
            letras_verificadas.append("("+palabra_ingresada[posicion]+")")

        # Si no se cumple ninguna condicion
        else:
            letras_verificadas.append(palabra_ingresada[posicion])

    return letras_verificadas

def imprimir_grilla(grilla):    
    for iterador in grilla:
        print(iterador)

# EJECUCION DEL PROGRAMA 

palabra_misteriosa = "squat"
cantidad_de_letras = 5
intentos = 6
grilla = []

print("Bienvenido a Wordle2.0")

while intentos > 0:
    print(f'Te quedan {intentos} intentos.')
    palabra_ingresada = input('Ingrese una palabra: ')
    intentos -= 1

    if (len(palabra_ingresada) != cantidad_de_letras):
        print("Ingrese una palabra con 5 caracteres")
        continue
    else:
        linea_verificada = verificacion_palabra(palabra_misteriosa, palabra_ingresada)
        grilla.append(linea_verificada)

    imprimir_grilla(grilla)

    if palabra_ingresada == palabra_misteriosa:
        print("Ganaste!!!!!!!!!!!!!!!!!!!!!!!!")
        break 