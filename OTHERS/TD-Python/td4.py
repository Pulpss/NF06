import math
import random

def exo21():
    dim1 = float(input("Entrez la dimension 1: "))
    dim2 = float(input("Entrez la dimension 2: "))
    dim3 = float(input("Entrez la dimension 3: "))

    def type(dim1, dim2, dim3):
        if dim1 == dim2 and dim2 == dim3:
            return "equilateral"
        elif dim1 == dim2 or dim2 == dim3 or dim1 == dim3:
            return "isocele"
        else:
            return "autre"

    def perimetre(dim1, dim2, dim3):
        return dim1 + dim2 + dim3

    def aire(dim1, dim2, dim3):
        p = perimetre(dim1, dim2, dim3) / 2
        return math.sqrt(p * (p - dim1) * (p - dim2) * (p - dim3))

    print("type: " + type(dim1, dim2, dim3))
    print("perimetre: " + str(perimetre(dim1, dim2, dim3)))
    print("aire: " + str(aire(dim1, dim2, dim3)))


def exo22():
    terme1 = float(input("Entrez le premier terme: "))
    raison = float(input("Entrez la raison: "))
    n = int(input("Entrez le nombre de terme: "))

    def terme(n, terme1, raison):
        return terme(n - 1, terme1, raison) * raison if n > 1 else terme1

    def listeTermes(n, terme1, raison):
        return [terme(ni, terme1, raison) for ni in range(1, n + 1)]

    def sommeTermes(termes):
        sum = 0
        for terme in termes:
            sum += terme
        return sum

    def sommeTermesForm(n, terme1, raison):
        return sum([(raison**ni) * terme1 for ni in range(0, n)])

    def suiteValide(liste):
        raison_possible = liste[0] / liste[1]
        for n in range(1, len(liste)):
            if liste[n] / liste[n + 1] != raison_possible:
                return False
        return True

    print("terme: " + str(terme(n, terme1, raison)))
    liste = listeTermes(n, terme1, raison)
    print("listeTermes: " + str(liste))
    print("sommeTermes: " + str(sommeTermes(liste)))
    print("sommeTermes: " + str(sommeTermesForm(n, terme1, raison)))

def exo23():
    liste = []

    def add_product(liste, product_name, quantity=1):
        for index in [
            i for i in range(len(liste)) if liste[i]["product_name"] == product_name
        ]:
            liste[index]["quantity"] += 1
        else:
            liste.append({"product_name": product_name, "quantity": quantity})
        return liste

    def remove_product(liste, product_name, quantity=1):
        for index in [
            i for i in range(len(liste)) if liste[i]["product_name"] == product_name
        ]:
            liste[index]["quantity"] -= quantity
        return liste

    def print_liste(liste):
        for product in liste:
            print(
                "Product name: "
                + product["product_name"]
                + " , Quantity: "
                + product["quantity"]
            )

def exo24():
    dictionnaire = [
        ["table", "un objet pour manger"],
        ["chaise", "un objet pour s'asseoir"],
        ["ordinateur", "un objet pour travailler"],
        ["livre", "un objet à lire"],
    ]
    def pick_word(dictionnaire):
        return dictionnaire[random.randint(0, len(dictionnaire) - 1)]
    def print_word(word):
        print("La longueur du mot est: " + str(len(word)) + " et sa description est: " + word[1])
    def game(dictionnaire):
        vies = 3
        res = pick_word(dictionnaire)
        guess = ""
        print_word(res)
        while vies != 0 and guess != res:
            lettre = input("Entrez une lettre: ")
            if guess + lettre == res[0]:
                print("Vous avez gagné")
                break
            elif guess + lettre in res[0]:
                print("La lettre était bonne, vous gagnez une vie")
                guess += lettre
                vies += 1
            else:
                vies -= 1
                print("La lettre était mauvaise, vous perdez une vie, il vous en reste " + str(vies))
        return
    game(dictionnaire)
exo = int(input("Quelle exo voulez vous lancer: "))

if exo == 20:
    exo20()
elif exo == 21:
    exo21()
elif exo == 22:
    exo22()
elif exo == 23:
    exo23()
elif exo == 24:
    exo24()
elif exo == 25:
    exo25()
elif exo == 26:
    exo26()
