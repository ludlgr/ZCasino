import os
from random import randint
from math import ceil

somme = 1000
nom = input("Comment vous appelez-vous ? ")

print(f"Bienvenue à la roulette du ZCasino, {nom} !")

while somme > 0:
    print(f"Vous disposez de {somme} jetons.")
    NGagnant = randint(0, 49)

    NMise = -1
    while NMise < 0:
        NMise = input(f"{nom}, veuillez miser sur une case entre 0 et 49. ")
        try:
            NMise = int(NMise)
            if NMise < 0 or NMise > 49:
                raise ValueError
        except ValueError:
            print("Merci d'indiquer une case valide.")
            NMise = -1
            continue

    Mise = -1
    while Mise < 0:
        Mise = input("Combien de jetons souhaitez-vous miser ? ")
        try:
            Mise = int(Mise)
            if Mise < 0 or Mise > somme:
                raise ValueError
        except ValueError:
            print("Merci de miser un montant de jetons adéquat.")
            Mise = -1
            continue
    
    print("Le croupier lance la roue...")
    os.system("pause")
    print("La roue tourne...")
    os.system("pause")
    print("La roue ralentit...")
    os.system("pause")
    print(f"La roue s'arrête sur la case {NGagnant} !")

    if NMise == NGagnant:
        print(f"Jackpot ! Vous avez misé sur la bonne case ! Vous remportez trois fois votre mise soit {3*Mise} jetons !")
        somme += 3 * Mise
    elif NMise % 2 == NGagnant % 2:
        print(f"Le numéro misé est de la même couleur que le numéro gagnant ! Vous remportez la moitié de votre mise soit {ceil(Mise*0.5)} jetons !")
        somme += ceil(Mise*0.5)
    else:
        print("Dommage ! Vous perdez votre mise :(")
        somme -= Mise

    if somme <= 0:
        print("Quel dommage ! Vous n'avez plus de jetons ! Fin de la partie :(")
        break

    print(f"Vous disposez maintenant de {somme} jetons.")
    
    quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
    if quitter == "o" or quitter == "O":
        print("Vous quittez le casino avec vos gains. À bientôt !")
        break


os.system("pause")
