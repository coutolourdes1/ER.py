import re
import sys

def prog(texto):

    match_patt = re.findall(r'("patterns":\s*\[(\s*".*",))', texto)
    match_resp = re.findall(r'("responses":\s*\[(\s*".*",))', texto)
 
    for x in range(len(match_patt)):
        sustituto = re.sub(r',', '', match_patt[x][0])
        texto = re.sub(r'("patterns":\s*\[(\s*".*",\s*)*(".*"))', sustituto, texto, count=1)
    
    for y in range(len(match_resp)):
        sustituto = re.sub(r',', '', match_resp[y][0])
        texto = re.sub(r'("responses":\s*\[(\s*".*",*\s*)*(".*"))', sustituto, texto, count=1)
    

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