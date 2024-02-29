adn = ["A","C","G","T","T","A","G","C","T","A","A","C","G"]
a=[]

for i in adn:
    if(i=="A"):
        a.append("T")
    elif(i=="T"):
        a.append("A")
    elif(i=="C"):
        a.append("G")
    elif(i=="G"):
        a.append("C")
print(adn,"\n est remplace par\n",a)