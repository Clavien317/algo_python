s=0
n=100
pair_liste =[]
impair_list=[]

while(s<n):
    s=s+1
    if(s%2==0 and s<=50):
        pair_liste.append(s)
    elif(s%2!=0 and s>50):
        impair_list.append(s)
print(pair_liste)
print(impair_list)