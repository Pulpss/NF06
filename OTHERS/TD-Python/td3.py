from datetime import date
import math


def exo13():
    liste = []
    nb = input("Entrez un nombre: ")
    while nb != "n":
        liste.append(int(nb))
        nb = input("Entrez un nombre (n pour quitter): ")
    print("La somme de la liste est: " + str(sum(liste)))
    print("La moyenne de la liste est: " + str(sum(liste) / len(liste)))
    mul = 1
    for i in liste:
        mul *= i
    print("Le produit de tous les nombres de la liste est: " + str(mul))
    cherche = int(input("Entrez un nombre a chercher: "))
    if cherche in liste:
        print("Votre nombre est dans la liste")
    else:
        print("Votre nombre n'est pa dans la liste")
    milieu = int(input("Entrez un nombre à inserer au milieu: "))
    liste.insert(len(liste) // 2, milieu)
    suppr = int(input("Entrez un nombre à supprimer s'il existe: "))
    if suppr in liste:
        liste.remove(suppr)
    else:
        print("Votre nombre n'est pas dans la liste")
    inf = int(input("Entrez une borne inferieur: "))
    sup = int(input("Entrez une borne superieure: "))
    print(liste[inf:sup])


def exo14():
    users = [
        ("Bob", ("Movies", "Football", "Reading")),
        ("Alice", ("Swimming", "Handball", "Gaming")),
        ("Eva", ("Movies", "Coding", "Gaming")),
    ]
    inp = input("Voulez vous entrer des utilisateurs additionels (n pour Non): ")
    while inp != "n":
        name = input("Entrez le nom de l'utilisateur: ")
        h1 = input("Entrez le hobby 1 de la personnne: ")
        h2 = input("Entrez le hobby 2 de la personnne: ")
        h3 = input("Entrez le hobby 3 de la personnne: ")
        users.append((name, (h1, h2, h3)))
        inp = input("Voulez vous entrer des utilisateurs additionels (n pour Non): ")
    print(users)
    cherch = input("Quelle activité voulez vous compter: ")
    count = 0
    for user in users:
        for hobby in user[1]:
            if hobby.find(cherch):
                count += 1
                break

    print("Il y a " + str(count))

    personne1 = int(input("Entrez le numéro de la personne 1: "))
    personne2 = int(input("Entrez le numéro de la personne 2: "))

    count = 0
    for hobby in users[personne1][1]:
        if hobby in users[personne2][1]:
            count += 1

    print("Il ont en commun " + str(count))

    suppr = int(input("Entrez le numéro de l'utilisateur qui n'aime plus: "))
    hob = input("Entrez le nom de l'activité qu'il n'aime plus: ")
    to_remove = users[suppr][1].index(hob)
    temp = users[suppr]
    new = (temp[0], *temp[1][0 : to_remove], *temp[1][to_remove + 1 :])
    users.remove(temp)
    users.insert(suppr, new)

    asupr = int(input("Entrez le numéro de l'utilisateur qui veut etre supprimer: "))
    users.remove(users[asupr])

    suppr = int(input("Entrez le numéro de l'utilisateur veut changer: "))
    hob = input("Entrez le nom de l'activité qu'il veu changer: ")
    newhob = input("Entrez le nom de la nouvelle activité: ")
    to_remove = users[suppr][1].index(hob)
    temp = users[suppr]
    new = (temp[0], *temp[1][0 : to_remove], newhob, *temp[1][to_remove + 1 :])
    users.remove(temp)
    users.insert(suppr, new)
    
    print(users)


def exo15():
    etus = [
        [
            {"demo": 10, "code": 10, "present": 11, "docu": 10},
            {"demo": 10, "code": 10, "present": 11, "docu": 11},
        ]
    ]

    sum = 0
    sumC = 0
    sumPy = 0
    for etu in etus:
        sum = 0
        for key in etu[0]:
            sum += etu[0][key]
        moy = sum / 4
        sumC += moy
        print(moy)
        sum = 0
        for key in etu[1]:
            sum += etu[1][key]
        moy = sum / 4
        sumPy += moy
        print(moy)
    moyC = sumC / len(etus)
    moyPy = sumPy / len(etus)
    print("La moyenne general en C est: " + str(moyC))
    print("La moyenne general en Py est: " + str(moyPy))
    coef = (moyC - moyPy) / moyC
    print((coef + 1) * moyPy)


def exo16():
    def addFilm(films):
        titre = input("Entrez le titre du film: ")
        annee = input("Entrez l'année du film: ")
        note = input("Entrez la note IMDB du film: ")
        copies = input("Entrez le nombre de copies du film: ")
        prix = input("Entrez le prix du film: ")
        duree = input("Entrez la durée du film: ")
        films.append(
            {
                "titre": titre,
                "annee": annee,
                "note": note,
                "copies": copies,
                "prix": prix,
                "duree": duree,
            }
        )
        return films

    def supprFilm(films):
        titre = input("Entrez le titre du film à supprimer: ")
        for film in films:
            if film["titre"] == titre:
                films.remove(film)
                break
        return films

    def afficheDispo(films):
        for film in films:
            if int(film["copies"]) > 0:
                print(
                    "Titre: "
                    + film["titre"]
                    + " Année: "
                    + film["annee"]
                    + " Note: "
                    + film["note"]
                    + " Copies: "
                    + film["copies"]
                    + " Prix: "
                    + film["prix"]
                    + " Durée: "
                    + film["duree"]
                )

    def afficeParOrdreNote(films):
        films.sort(key=lambda x: x["note"], reverse=True)
        for film in films:
            print(
                "Titre: "
                + film["titre"]
                + " Année: "
                + film["annee"]
                + " Note: "
                + film["note"]
                + " Copies: "
                + film["copies"]
                + " Prix: "
                + film["prix"]
                + " Durée: "
                + film["duree"]
            )
    def louerFilm(films):
        titre = input("Entrez le titre du film à louer: ")
        for film in films:
            if film["titre"] == titre:
                film["copies"] = int(film["copies"]) - 1
                break
        return films


exo = int(input("Quelle exo voulez vous lancer: "))

if exo == 13:
    exo13()
elif exo == 14:
    exo14()
elif exo == 15:
    exo15()
elif exo == 16:
    exo16()
