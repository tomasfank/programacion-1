""" Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. Tener en cuenta que los comentarios comienzan con el signo # (siempre que éste no se encuentre encerrado entre comillas simples o dobles) y que también se considera comentario a las cadenas de documentación (docstrings)."""

# 3 etapas en el trabajo con archivos= 1) apertura 2) procesamiento 3) cierre.

# durante la apertura del archivo se especifican dos parámetros= 1) la ruta del archivo 2) modo de apertura. 

def eliminar_comentarios(codigo):
    lineaNueva = ""
    comillasDobles = False
    comillasSimples = False
    for x in range(len(codigo)):
        caracter = codigo[x]

        if caracter == "'" and not comillasDobles:
            comillasSimples = not comillasSimples

        elif caracter == '"' and not comillasSimples:
            comillasDobles = not comillasDobles

        elif caracter == '#' and not(comillasSimples or comillasDobles):
            lineaNueva = codigo[:x]
            break
        else:
            lineaNueva = codigo
    return lineaNueva

    

try:
    entrada = open("miprograma.txt", "rt")
    salida = open("miprogramasincomentario.txt", "wt")

    for linea in entrada:
        comprobar_linea = eliminar_comentarios(linea)
        salida.write(comprobar_linea)
    
except FileNotFoundError as mensaje:
    print("No se puede abrir el archivo:", mensaje)
except OSError as mensaje:
    print("Error:", mensaje)
#debido a la importancia del cierre se suele realizar en la clausula fynally     
else:
    print("Copia finalizada")
finally:
    try:
        entrada.close()
        salida.close()
    except NameError:
        pass