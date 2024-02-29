

p = float(input("Entrer la pression du courant ? \n"))
v=float(input("Entrer le volume : \n"))

ps=2.3
vs = 7.41

if(p>ps and v>vs):
    print("Arret immediatement ...")
elif(p>ps):
    print("demande d'augmentation de volume de l'enceinte")
elif(v>vs):
    print("demande de diminution de volume de l'enceinte")
else:
    print("Tout va bien")