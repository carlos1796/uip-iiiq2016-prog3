x=True
agua=0
fuego=0
lista=[]
while x:
    a=input()
    if a=="salir":
        break
    if a.find("fuego")!=-1:
        fuego=fuego+1
        lista.append(a)
    if a.find("agua")!=-1:
        agua=agua+1
        lista.append(a)
print ("Agua: " + str(agua))
print ("Fuego: "+ str(fuego))
print (lista)




