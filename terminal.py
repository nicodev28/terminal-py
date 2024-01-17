# Terminal with python
import os
import subprocess

# Run command

while True:
    command = input(os.getcwd() + "-> ")
    if command == "q":
        break
    
    command_split = command.split(" ")
    if len(command_split) == 2 and command_split[0] == "cd":
        try:
            os.chdir(command_split[1])
        except FileNotFoundError:
            print("Erreur: Le dossier n'existe pas!")
            print("q pour quitter le programme")
            
    else:
        resultat = subprocess.run(command, shell=True, capture_output=True, universal_newlines=True)
        print("")
        print(resultat.stdout)
        print(resultat.stderr)
        print("q pour quitter le programme")
        print("")
