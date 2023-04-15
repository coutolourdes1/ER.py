import re
import sys

total1 = 0
total2 = 0
total3 = 0

def stringFromMatch(match):
    global total1, total2, total3
    resp = re.sub(r'([a-zA-Z0-9],)', '', match[6])  
    # Sumar a las variables globales
    total1 += 1
    total2 += len(match[3].split(','))
    total3 += len(resp.split(r','))
    return f" 1 {len(match[3].split(','))} {len(resp.split(r','))}"
    
def prog(texto):
    global total1, total2, total3
    matches = re.findall(r'{\s*("tag": ("(.+)")),\s*("patterns":\s*\[\s*(".*",{0,1}\s*)*)(.|\s)*?,\s*("responses":\s*\[\s*(".*",{0,1}\s*)*)(.|\s)*?}', texto)

    result = '\n'.join(map(stringFromMatch, matches))
    return f"{total1} {total2} {total3}"


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
