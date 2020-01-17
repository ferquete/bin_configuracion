#!/usr/bin/python3

import time
import subprocess as sp
import shlex


def ejecutarComando(s):
    return sp.run(shlex.split(s), stdout=sp.PIPE)


def messagePeligro(msg):
    ejecutarComando("notify-send -u critical '"+msg+"'")
    ejecutarComando("espeak -ves 'Batería'")


def obtenerListaComando():
    ret = ejecutarComando('acpi -b')
    ret = ret.stdout.decode('UTF-8')
    return ret.split(',')


def isCargando(lista):
    if "Charging" in lista[0]:
        return True
    return False


def getPorcentage(lista):
    p = lista[1].strip().replace("%", "")
    return int(p)


def accionesSegunPorcentage(v, isCarg):
    if v <= 6 and isCarg is False:
        messagePeligro("Batería por debajo del 6% !!!!!!")


if __name__ == "__main__":
    while True:
        lista = obtenerListaComando()
        valor = getPorcentage(lista)
        isCarg = isCargando(lista)
        accionesSegunPorcentage(valor, isCarg)
        time.sleep(10)

