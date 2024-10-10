import sys
from math import *
from operator import truediv
from zipimport import alt_path_sep

"""def Hello(nom, age, AnneeNaissance):
    if nom == "joe":
        print("Hello joe, Welcome to the world")
        print("Bonjour Joe, l'apostrophe, c'est cool !")
        print('Bonjour Joe, comme diraient certains : "quelle belle journée" !')
        print('Bonjour Joe, comme dirait l\'autre : "c\'est une belle journée"')
        print(nom + " est né en " + str(AnneeNaissance))
    else:
        print("Hello World")


nom = sys.stdin.readline().strip()
age = int(sys.stdin.readline().strip())
AnneeNaissance = int(sys.stdin.readline().strip())
Hello(nom, age, AnneeNaissance)


def perimetrecercle(r):
    return r * 2 * pi

print(perimetrecercle(5))

def vitesse(tmps, dist):
    return (dist/tmps * 3.6)

print(vitesse(50, 40))

def longueurPisteCourse(r, l):
    return perimetrecercle(r) + l*2

print(longueurPisteCourse(5, 5))


def vitesse2(r,l ,tmps):
    return vitesse(tmps, longueurPisteCourse(r,l))

print(vitesse2(200, 900, 600))

def Coureurs(r, l):
    lst = []
    for compteur in range(0,5):
        print("donner un temps", compteur)
        lst.append(int(input()))
    for i in range(0,(len(lst))):
        lst[i] = vitesse2(r,l,lst[i])
    return lst

def Coureurs2(r, l):
    Coureurs = []
    for compteur in range(0, 5):
        print("donner un temps", compteur)
        Coureurs.append(int(input()))
    vitesses = []
    for temps in lst:
        vitesses.append(vitesse2(r,l,lst[i]))

r = int(input("rayon du terrain"))
l = int(input("longeur du terrain"))
print(Coureurs(r, l))

print("+-------------------------------------------------+")
print("+               CALCULATEUR                       +")
print("+-------------------------------------------------+")

def SaisirEntier():
    a = int(input("Saisir un entier : "))
    return a

def Calcul():
    nb1 = SaisirEntier()
    nb2 = SaisirEntier()
    a = print(nb1, "+", nb2, "=", nb1 + nb2)
    b = print(nb1, "-", nb2, "=", nb1 - nb2)
    c = print(nb1,"x", nb2, "=", nb1 * nb2)
    if nb2 != 0:
        d = print(nb1, "/", nb2, "=", nb1 / nb2)
        return a, b, c, d
    else:
        return a, b, c
    
Calcul()

def EstPair():
    nb = int(input("Nombre d'entiers : "))
    if nb%2 == 0:
        return True
    else:
        return False

#print(EstPair())

def max(a, b):
    if a > b:
        return a
    else:
        return b

def ToutLesPairs(x):
    if x % 2 == 0:
        while x != 0:
            return x - 2
    else:
        x = x - 1
        while x != 0:
            print(x)
            return x - 2

#print(ToutLesPairs(5))

def factorielle(n):
    a = 1
    for i in range(0, n):
        a = a * n
        n = n - 1
    return a

print(factorielle(5))
print(5 * 4 * 3 * 2)

def EstPremier(x):
    if x % 2 == 0 or x % 3 == 0:
        return False
    else:
        return True

print(EstPremier(11))

import random

def nb_aleatoire():
    nb = random.randint(1, 100)
    return nb

def Deviner(n, nd):
    if nd > n:
        print("nombre trop petit : ")
        return False
    elif nd < n:
        print("nombre trop grand : ")
        return False
    else:
        return True

def recuperer():
    a = int(input("Saisir un nombre : "))
    return a

def jouer():
    nb_deviner = nb_aleatoire()
    nb_coups = 0
    result = False
    while not result == True:
        nb = recuperer()
        Deviner(nb, nb_deviner)
        nb_coups += 1
        if nb == nb_deviner:
            result = True
    return result


print(jouer())"""

def triangle(x):
    for i in range(1, x + 1):
        print("#" * i)

triangle(5)

def pyramide(x):
    for i in range(x, 0, -1):
        print("#" * i)

print(pyramide(5))

"""def pyramide(x):
    for i in range(0, x, 1):
        print(" " * (x - i) + "#" * (i * 2 + 1)) 

x = int(input("quelle hauteur ?"))

pyramide(x)"""

def pyramide(x):
    for i in range(x, 0, -1):
        print(" " * (x - i) + "#" * (i * 2 - 1))

x = int(input("quelle hauteur ?"))

pyramide(x)

print('\n')




