#!/usr/bin/python3
#import os
#comentario = input("Comentario: ")

#if comentario:
#    os.system("git add -A && git commit -m \"{comentario}\" && git push -u origin master")
#else:
#    print("Error!")
import subprocess
import os


comentario = input("Comentario: ")
if comentario:
    os.system("git add -A && git commit -m \"{comentario}\"")
    p = subprocess.run(["git","push","-u","origin","master"],
                       stdout=subprocess.PIPE)
    print(p.stdout)
else:
    print("Error! se necesita un comentario...")
    exit(1)