from datetime import date
import math


def exo1():
  email = str(input("Entrez votre email: "))
  print("Bonjour UTT " + str(date.today()) + " " + email)

  nom = str(input("Entrez votre nom: "))
  prenom = str(input("Entrez votre prenom: "))
  etude = str(input("Entrez votre nombre d'années d'étude: "))
  language = str(input("Entrez votre language de programmation préféré: "))

  print("Bonjour " + prenom + nom +
        ", j'espere que tu es content d'avoir fait " + etude +
        " années d'étude, et le language " + language +
        " est le pire language de programmation")


def exo2():
  a = 0
  b = 1.2
  c = "abc"
  d = False
  d = bool(a)
  b = float(a)
  print("type a: " + str(type(a)))
  print("type b: " + str(type(b)))
  print("type c: " + str(type(c)))
  print("type d: " + str(type(d)))
  print("d: " + str(d))
  print("b: " + str(b))
  # c'est possible d'assigner un int a un booleen si on le converti d'abord et que l'entier est 1 ou 0

  # il est possible d'assigner un entier à un float en le convertissant
  b_int = int(a)
  a_float = float(b)

  print("a_int: " + str(a_float))
  print("b_int: " + str(b_int))

  b_str = str(a)
  a_str = str(b)

  print("a_str: " + a_str)
  print("b_str: " + b_str)


def exo3():
  nbA = int(input("Entrez un premier nombre: "))
  nbB = int(input("Entrez un deuxième nombre: "))
  print("somme: " + str(nbA + nbB))
  print("difference: " + str(nbA - nbB))
  print("produit: " + str(nbA * nbB))
  print("division: " + str(nbA / nbB))
  print("quotient: " + str(nbA // nbB))
  print("reste: " + str(nbA % nbB))

  base = float(input("Entrez la base du triangle"))
  hauteur = float(input("Entrez la hauteur du triangle"))

  print("La surface du triangle est: " + str(base * hauteur / 2))

  rayon = float(input("Entrez le rayon du cone"))
  hauteurcone = float(input("Entrez la hauteur du cone"))

  print("Le volume du cone est: " +
        str((1 / 3) * math.pi * rayon * rayon * hauteurcone))

  varA = float(input("Entrez la variable A"))
  varB = float(input("Entrez la variable B"))

  varA, varB = varB, varA

  print("variable A: " + str(varA))
  print("variable B: " + str(varB))


def exo4():
  chaine = input("Entrez une chaine de caractères: ")
  print("La longueur de la chaine est: " + str(len(chaine)))
  chaine2 = input("Entrez une autre chaine de caractère: ")
  print("Les deux chaines concatenées sont: " + chaine + chaine2)
  recherche = input(
    "Que voulez vous remplacez dans la chaine de caractère 1: ")
  remplacement = input(
    "Par quoi voulez vous remplacer dans la chaine de caractère 1: ")
  print("La chaine 1 remplacée est: " +
        chaine.replace(recherche, remplacement))
  print("La chaine 2 en majuscule est: " + str(chaine2.upper()))
  print("La chaine 1 en minuscule est: " + str(chaine.lower()))
  print("La chaine 1 en minuscule est: " + str(chaine.title()))

  mots = chaine.split(' ')
  for mot in mots:
    print(mot)


exo = int(input("Quelle exo voulez vous lancer: "))

if (exo == 1):
  exo1()
elif (exo == 2):
  exo2()
elif (exo == 3):
  exo3()
elif (exo == 4):
  exo4()
