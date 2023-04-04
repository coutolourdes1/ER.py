# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):


    match = re.findall(r'("tag": "(.*)",)\n(.|S)*"patterns": \[((?:\s*".*?"\s*,)*\s*".*?"\s*)\]', texto)
    lista = ' '.join(match[0][3])
    exp = re.findall(r'(".*"[^:])', lista)
    cant = len(exp)
    ret = ' '.join(match[0][1])

    return ret + " " + str(cant) + "\n"

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)      # ejecutar er
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
