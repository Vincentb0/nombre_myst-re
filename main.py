# """
# Jeu du nombre mystère.
# """
# import random, sys
#
# nombre_mystere = random.randint(1, 10)
# question = ""
# compteur_vies = 5
#
# while True:
#     print(f"Il te reste {compteur_vies} vie{'s' if compteur_vies > 1 else ''}")
#     question = input("Devine le nombre : ")
#     if not question.isdigit():
#         print("Erreur, entre un nombre valide ...")
#     elif question.isdigit():
#         question = int(question)
#         if question > nombre_mystere:
#             print("Le nombre mystère est plus petit")
#             compteur_vies -= 1
#         elif question < nombre_mystere:
#             print("Le nombre mystère est plus grand")
#             compteur_vies -= 1
#         else:
#             print("Bravo, tu as trouvé le nombre mystère")
#             exit()
#
#     print()
#
#     if compteur_vies == 0:
#         print(f"Tu as perdu ..., le nombre mystère était {nombre_mystere}")
#         exit()


# --------------- AUTRE METHODE ---------------

from random import randint
from sys import exit

nombre_mystere = randint(0, 10)
question = ""
nombre_vies = 5

while nombre_vies > 0:
    print(f"Il te reste {nombre_vies} vie{'s' if nombre_vies > 1 else ''}")
    question = input("Devine le nombre : ")
    while not question.isdigit():
        print("Erreur, entre un nombre valide ...")
        question = input("Devine le nombre : ")

    if question.isdigit():
        question = int(question)
        if question > nombre_mystere:
            print("Le nombre mystère est plus petit")
        elif question < nombre_mystere:
            print("Le nombre mystère est plus grand")
        else:
            print("Bravo, tu as trouvé le nombre mystère")
            exit()

    print()
    nombre_vies -= 1

    if nombre_vies == 0:
        print(f"Tu as perdu, le nombre mystère était : {nombre_mystere}")


