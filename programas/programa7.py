import re
import sys


def prog(texto):

    texto = re.sub(r'"tag": ".+",', '"tag": "T",', texto)
    texto = re.sub(
        r'("patterns":\s*(\[\s*((".*",{0,1}\s*))*\]))', '"patterns": [\n      "P"\n   ]', texto)
    texto = re.sub(
        r'("responses":\s*(\[\s*((".*",{0,1}\s*))*\]))', '"responses": [\n      "R"\n   ]', texto)
    return texto


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)

    f = open(entrada, 'r')  # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada

    ret = prog(datos)      # ejecutar er

    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
