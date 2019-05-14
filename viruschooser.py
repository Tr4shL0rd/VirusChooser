import time
import os
import datetime
import pyfiglet


name = pyfiglet.figlet_format("Virus Chooser", font = "slant")
clear = "\n" * 100

print(clear)
print(name)


print("choose a virus!")
print()
#print("Sp4ceDestr0yer")
print("SpaceDestroyer")
print("50/50")
print()
chooser = input("what virus do you want to see? ")

if chooser == "SpaceDestroyer":
    os.system('python spammer.py')
elif chooser == "50/50":
    os.system('python 5050.py')
elif chooser == "meme":
    os.system('terminal-parrot')
