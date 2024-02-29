j7 = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

while True:
    j = input("Entrer un jour de la semaine (ou 'quitter' pour sortir) : ")
    if j.lower() == "quitter":
        print("Bye !")
        break
    elif j.lower() in j7:
        if j.lower() in ["lundi", "mardi", "mercredi", "jeudi"]:
            print("Au travail")
        elif j.lower() == "vendredi":
            print("Chouette c'est vendredi")
        else:
            print("Repos ce week-end")
    else:
        print("Entrée invalide")