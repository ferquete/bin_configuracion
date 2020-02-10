#!/usr/bin/python3
import os
comentario = input("Comentario: ")

if comentario:
    os.system("git add -A && git commit -m \"{comentario}\" && git push -u origin master")
else:
    print("Error!")
