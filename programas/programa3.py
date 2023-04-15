import re
import sys


def stringFromMatch(match):
    return f"{match[2]} {len(match[3].split(','))}"


def prog(texto):

    matches = re.findall(r'{\s*("tag": ("(.+)")),\s*("patterns":\s*\[\s*(".*",{0,1}\s*)*)(.|\s)*?}', texto)

    result = '\n'.join(map(stringFromMatch, matches))
    return result


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