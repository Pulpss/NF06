from math import sqrt
import cmath
import re
from random import randint


def exo5():
    nom = input("Entrez votre nom: ")
    taille = float(input("Entrez votre taille en cm: "))
    age = int(input("Entrez votre âge: "))

    if len(nom) > 20:
        print("Votre nom est long.")
    elif len(nom) > 15:
        print("Votre nom est moyen.")
    elif len(nom) == 8 or len(nom) == 9 or len(nom) == 10:
        print("Votre nom est semi court.")
    else:
        print("Votre nom est court.")

    if age < 18:
        print("Vous êtes mineur.")

    if taille > 172:
        print("Vous êtes grand.")


def exo6():
    nombre = int(input("Entrez un nombre: "))
    if nombre > 0:
        print("Le nombre est positif.")
    elif nombre < 0:
        print("Le nombre est négatif.")
    else:
        print("Le nombre est nul.")
    if nombre % 2 == 0:
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")
    for i in range(1, sqrt(nombre)):
        if nombre % i == 0:
            print("Le nombre n'est pas premier.")
            break


def exo7():
    mdp = input("Entrez un mot de passe: ")
    if re.match(
        r"(?=.*[a-z]{2})(?=.*[A-Z]{2})(?=.*[0-9]{2})(?=.*[!@#$%^&*()_+}{:;?><])(?=.{6,16})",
        mdp,
    ):
        print("Le mot de passe est valide.")


def exo8():
    a = float(input("Entrez le coefficient a: "))
    b = float(input("Entrez le coefficient b: "))
    c = float(input("Entrez le coefficient c: "))
    delta = b * b - 4 * a * c
    if delta < 0:
        sol1 = (-b - cmath.sqrt(delta)) / (2 * a)
        sol2 = (-b + cmath.sqrt(delta)) / (2 * a)
        print("Les solutions sont: ", sol1, " et ", sol2)
    else:
        sol1 = (-b - cmath.sqrt(delta)) / (2 * a)
        sol2 = (-b + cmath.sqrt(delta)) / (2 * a)
        print("Les solutions sont: ", sol1, " et ", sol2)


def exo9():
    random = randint(1, 100)
    ask = int(input("Entrez un nombre: "))
    while ask != random:
        if ask < random:
            print("Le nombre est plus grand.")
        else:
            print("Le nombre est plus petit.")
        ask = int(input("Entrez un nombre: "))


def exo10():
    def fibo(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fibo(n - 1) + fibo(n - 2)

    n = int(input("Entrez un nombre: "))
    print(fibo(n))


def exo11():
    def combinaison(p, n):
        if p == 0 or n == p:
            return 1
        else:
            return combinaison(p - 1, n - 1) + combinaison(p, n - 1)
    p = int(input("Entrez le nombre p: "))
    n = int(input("Entrez le nombre n: "))
    print(combinaison(n, p))

def exo12():
    somme = 0
    texte = input("Entrez un texte: ")
    print("Il y a ce nombre de mots: "+str(len(re.findall(r"[' ']", texte))+1))
    print("Il y a ce nombre de voyelles: "+str(len(re.findall(r"[aeiouy]", texte))))
    mots = texte.split(" ")
    for mot in mots:
        if len(re.findall(r"[aeiouy]+", mot)) > 1:
            somme += 1
    print("Il y a ce nombre de mots avec deux voyelles: "+str(somme))



exo = int(input("Quelle exo voulez vous lancer: "))

if exo == 5:
    exo5()
elif exo == 6:
    exo6()
elif exo == 7:
    exo7()
elif exo == 8:
    exo8()
elif exo == 9:
    exo9()
elif exo == 10:
    exo10()
elif exo == 11:
    exo11()
elif exo == 12:
    exo12()
