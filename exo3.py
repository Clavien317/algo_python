note = [14, 9, 13, 15, 12]

max = max(note)
min = min(note)

total =0
nbmat = len(note)

print("Nombre de matiere est :",nbmat)

for i in note:
    total=total+i
moyenne = total/nbmat


print("Note maximum de ce etudiant est : ",max)
print("Note minimum de ce etudiant est : ",min)

print("Moyenne de ce etudiant est : ",moyenne)
if(moyenne>=10 and moyenne<12):
    print("Mention passable")
elif(moyenne>=12 and moyenne<14):
    print("Mention assez-bien")
elif(moyenne>=14 and moyenne<16):
    print("Mention bien")
elif(moyenne>=16):
    print("Mention tres bien")