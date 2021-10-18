import time
import os
import math
from datetime import datetime
version = "1.01"
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
clear = lambda: os.system("cls")
pi = math.pi

def load():
    print(pi)
    print("Loading Assets")
    time.sleep(.1)
    print("Loading Application")
    time.sleep(.1)
    print("Loading Extras")
    time.sleep(.1)
    print("Loading Loops")
    time.sleep(.1)
    print("Loading Imports")
    time.sleep(.1)
    print("Loading Variables")
    time.sleep(.1)
    print("Loading Junk")
    time.sleep(1)
    print("Loading Responses")
    time.sleep(.1)
    print("Loading Functions")
    time.sleep(.1)
    print("Loading Tables")
    time.sleep(.1)
    print("Loading Modules")
    time.sleep(1)
    print("Loading Tips")
    time.sleep(.1)
    print("Loading Code")
    time.sleep(.1)
    print("Loading Python")
    time.sleep(3)
    clear()
    print(" ")

print("Please Wait")
time.sleep(3)

#Loading Imports
path = os.getcwd()+"\Loadup.txt"
print(path)

if os.path.exists(path):
    print("Path found")
    clear()
else:
    print("Loading")
    loadup = open('Loadup.txt', 'w')
    loadup.write("Current: ")
    loadup.write(current_time)
    loadup.write(" Version: ")
    loadup.write(version)






    loadup.close()
    load()
    clear()


print("Loaded")
clear()
print("Select language:")
print("A: FR")
print("B: ENG (Buggy)")
Language = input(": ")
clear()

if Language == "A":
    def start():
        print("Veuillez choisir votre option:")
        print("A: Calcule perimetre, aire d'un rectangle")
        print("B: Calcule perimetre, aire d'un care")
        print("C: Calcule perimetre, aire d'un cercle")
        als = input(": ")

        if als == "A":
            def start1():
                longeur = float(input("Longeur: "))
                largeur = float(input("Largeur: "))
                aire = longeur * largeur
                perimetre = (longeur + largeur) * 2
                print(" ")
                print("Calcul de l'aire d'un rectangle: ", longeur, "x", largeur)
                print("Calcul de perimetre d'un rectangle: ", longeur, "+", largeur, "x 2")
                print(" ")
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option1 = input(": ")
                if option1 == "A":
                    clear()
                    start1()
                elif option1 == "B":
                    clear()
                    start()
                elif option1 == "a":
                    clear()
                    start1()
                elif option1 == "b":
                    clear()
                    start()
            start1()
        elif als == "B":
            def start2():
                cote = float(input("Cote: "))
                print(" ")
                print("Calcul de l'aire d'un carre: ", "4", "x", cote)
                print("Calcul de perimetre d'un carre: ", cote, "x", cote)
                print(" ")
                aire = 4*cote
                perimetre = cote*cote
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start2()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start2()
                elif option2 == "b":
                    clear()
                    start()
            start2()
        elif als == "C":
            def start3():
                rayon = float(input("Rayon: "))
                diametre = float(input("Diametre: "))
                print(" ")
                print("Calcul de l'aire d'un cercle: ", "π", "x", rayon, "x", rayon)
                print("Calcul de perimetre d'un cercle: ","π", "x", diametre)
                print(" ")
                aire = pi*(rayon*rayon)
                perimetre = pi*diametre
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start3()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start3()
                elif option2 == "b":
                    clear()
                    start()
            start3()

        if als == "a":
            def start1():
                longeur = float(input("Longeur: "))
                largeur = float(input("Largeur: "))
                aire = longeur * largeur
                perimetre = (longeur + largeur) * 2
                print(" ")
                print("Calcul de l'aire d'un rectangle: ", longeur, "x", largeur)
                print("Calcul de perimetre d'un rectangle: ", longeur, "+", largeur, "x 2")
                print(" ")
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option1 = input(": ")
                if option1 == "A":
                    clear()
                    start1()
                elif option1 == "B":
                    clear()
                    start()
                elif option1 == "a":
                    clear()
                    start1()
                elif option1 == "b":
                    clear()
                    start()
            start1()
        elif als == "b":
            def start2():
                cote = float(input("Cote: "))
                print(" ")
                print("Calcul de l'aire d'un carre: ", "4", "x", cote)
                print("Calcul de perimetre d'un carre: ", cote, "x", cote)
                print(" ")
                aire = 4*cote
                perimetre = cote*cote
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start2()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start2()
                elif option2 == "b":
                    clear()
                    start()
            start2()
        elif als == "c":
            def start3():
                rayon = float(input("Rayon: "))
                diametre = float(input("Diametre: "))
                print(" ")
                print("Calcul de l'aire d'un cercle: ", "π", "x", rayon, "x", rayon)
                print("Calcul de perimetre d'un cercle: ","π", "x", diametre)
                print(" ")
                aire = pi*(rayon*rayon)
                perimetre = pi*diametre
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start3()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start3()
                elif option2 == "b":
                    clear()
                    start()
            start3()

    start()
if Language == "a":
    def start():
        print("Veuillez choisir votre option:")
        print("A: Calcule perimetre, aire d'un rectangle")
        print("B: Calcule perimetre, aire d'un care")
        print("C: Calcule perimetre, aire d'un cercle")
        als = input(": ")

        if als == "A":
            def start1():
                longeur = float(input("Longeur: "))
                largeur = float(input("Largeur: "))
                aire = longeur * largeur
                perimetre = (longeur + largeur) * 2
                print(" ")
                print("Calcul de l'aire d'un rectangle: ", longeur, "x", largeur)
                print("Calcul de perimetre d'un rectangle: ", longeur, "+", largeur, "x 2")
                print(" ")
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option1 = input(": ")
                if option1 == "A":
                    clear()
                    start1()
                elif option1 == "B":
                    clear()
                    start()
                elif option1 == "a":
                    clear()
                    start1()
                elif option1 == "b":
                    clear()
                    start()

            start1()
        elif als == "B":
            def start2():
                cote = float(input("Cote: "))
                print(" ")
                print("Calcul de l'aire d'un carre: ", "4", "x", cote)
                print("Calcul de perimetre d'un carre: ", cote, "x", cote)
                print(" ")
                aire = 4 * cote
                perimetre = cote * cote
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start2()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start2()
                elif option2 == "b":
                    clear()
                    start()

            start2()
        elif als == "C":
            def start3():
                rayon = float(input("Rayon: "))
                diametre = float(input("Diametre: "))
                print(" ")
                print("Calcul de l'aire d'un cercle: ", "π", "x", rayon, "x", rayon)
                print("Calcul de perimetre d'un cercle: ", "π", "x", diametre)
                print(" ")
                aire = pi * (rayon * rayon)
                perimetre = pi * diametre
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start3()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start3()
                elif option2 == "b":
                    clear()
                    start()

            start3()

        if als == "a":
            def start1():
                longeur = float(input("Longeur: "))
                largeur = float(input("Largeur: "))
                aire = longeur * largeur
                perimetre = (longeur + largeur) * 2
                print(" ")
                print("Calcul de l'aire d'un rectangle: ", longeur, "x", largeur)
                print("Calcul de perimetre d'un rectangle: ", longeur, "+", largeur, "x 2")
                print(" ")
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option1 = input(": ")
                if option1 == "A":
                    clear()
                    start1()
                elif option1 == "B":
                    clear()
                    start()
                elif option1 == "a":
                    clear()
                    start1()
                elif option1 == "b":
                    clear()
                    start()

            start1()
        elif als == "b":
            def start2():
                cote = float(input("Cote: "))
                print(" ")
                print("Calcul de l'aire d'un carre: ", "4", "x", cote)
                print("Calcul de perimetre d'un carre: ", cote, "x", cote)
                print(" ")
                aire = 4 * cote
                perimetre = cote * cote
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start2()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start2()
                elif option2 == "b":
                    clear()
                    start()

            start2()
        elif als == "c":
            def start3():
                rayon = float(input("Rayon: "))
                diametre = float(input("Diametre: "))
                print(" ")
                print("Calcul de l'aire d'un cercle: ", "π", "x", rayon, "x", rayon)
                print("Calcul de perimetre d'un cercle: ", "π", "x", diametre)
                print(" ")
                aire = pi * (rayon * rayon)
                perimetre = pi * diametre
                print("L'aire: ", aire)
                print("Perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Recommencer")
                print("B: Retour")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start3()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start3()
                elif option2 == "b":
                    clear()
                    start()

            start3()


    start()
if Language == "B":
    def start():
        print("Please select an option:")
        print("A: Calculate the perimeter, air of a rectangle")
        print("B: Calculate the perimeter, air of a square")
        print("C: Calculate the perimeter, air of a cercle")
        als = input(": ")

        if als == "a":
            def start1():
                longeur = float(input("Length : "))
                largeur = float(input("width : "))
                aire = longeur * largeur
                perimetre = (longeur + largeur) * 2
                print(" ")
                print("Calculation the air of a rectangle: ", longeur, "x", largeur)
                print("Calculation the perimeter of a rectangle: ", longeur, "+", largeur, "x 2")
                print(" ")
                print("The air: ", aire)
                print("The perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Restart")
                print("B: Back")
                option1 = input(": ")
                if option1 == "A":
                    clear()
                    start1()
                elif option1 == "B":
                    clear()
                    start()
                elif option1 == "a":
                    clear()
                    start1()
                elif option1 == "b":
                    clear()
                    start()

            start1()
        elif als == "b":
            def start2():
                cote = float(input("Side: "))
                print(" ")
                print("Calculation de the air of a square: ", "4", "x", cote)
                print("Calculation the perimeter of a square: ", cote, "x", cote)
                print(" ")
                aire = 4 * cote
                perimetre = cote * cote
                print("The air: ", aire)
                print("The perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Restart")
                print("B: Back")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start2()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start2()
                elif option2 == "b":
                    clear()
                    start()

            start2()
        elif als == "c":
            def start3():
                rayon = float(input("Rayon: "))
                diametre = float(input("Diameter: "))
                print(" ")
                print("Calculation the air of a circle: ", "π", "x", rayon, "x", rayon)
                print("Calculation the perimeter of a circle: ", "π", "x", diametre)
                print(" ")
                aire = pi * (rayon * rayon)
                perimetre = pi * diametre
                print("The air: ", aire)
                print("The perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Restart")
                print("B: Back")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start3()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start3()
                elif option2 == "b":
                    clear()
                    start()

            start3()

        elif als == "A":
            def start1():
                longeur = float(input("Length : "))
                largeur = float(input("width : "))
                aire = longeur * largeur
                perimetre = (longeur + largeur) * 2
                print(" ")
                print("Calculation the air of a rectangle: ", longeur, "x", largeur)
                print("Calculation the perimeter of a rectangle: ", longeur, "+", largeur, "x 2")
                print(" ")
                print("The air: ", aire)
                print("The perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Restart")
                print("B: Back")
                option1 = input(": ")
                if option1 == "A":
                    clear()
                    start1()
                elif option1 == "B":
                    clear()
                    start()
                elif option1 == "a":
                    clear()
                    start1()
                elif option1 == "b":
                    clear()
                    start()

            start1()
        elif als == "B":
            def start2():
                cote = float(input("Side: "))
                print(" ")
                print("Calculation de the air of a square: ", "4", "x", cote)
                print("Calculation the perimeter of a square: ", cote, "x", cote)
                print(" ")
                aire = 4 * cote
                perimetre = cote * cote
                print("The air: ", aire)
                print("The perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Restart")
                print("B: Back")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start2()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start2()
                elif option2 == "b":
                    clear()
                    start()

            start2()
        elif als == "C":
            def start3():
                rayon = float(input("Rayon: "))
                diametre = float(input("Diameter: "))
                print(" ")
                print("Calculation the air of a circle: ", "π", "x", rayon, "x", rayon)
                print("Calculation the perimeter of a circle: ", "π", "x", diametre)
                print(" ")
                aire = pi * (rayon * rayon)
                perimetre = pi * diametre
                print("The air: ", aire)
                print("The perimetre: ", perimetre)
                time.sleep(1)
                print(" ")
                print("A: Restart")
                print("B: Back")
                option2 = input(": ")
                if option2 == "A":
                    clear()
                    start3()
                elif option2 == "B":
                    clear()
                    start()
                elif option2 == "a":
                    clear()
                    start3()
                elif option2 == "b":
                    clear()
                    start()

            start3()



    start()




