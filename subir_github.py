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
                       input="ferquete\n66qbcqbcGithub??\n",
                       stdout=subprocess.PIPE,
                       shell=True)
    print(p.stdout)
else:
    print("Error! se necesita un comentario...")
    exit(1)