def muerto():
    f = open("temp.dat", "a")
    f.write(str(t) + ", Esta muerto\n")
    f.close()
def enf():
    f = open("temp.dat", "a")
    f.write(str(t) + ", Esta enfermo\n")
    f.close()
def normal():
    f = open("temp.dat", "a")
    f.write(str(t) + ", Normal\n")
    f.close()
def tf():
    f = open("temp.dat", "a")
    f.write(str(t) + ", Tiene Fiebre\n")
    f.close()

x=0
y=True
a=int(input("¿Cuantas temperaturas ingresara?"))
while x<a:
    try:
        t = float(input())
        if t <= 5:
            muerto()
        elif t > 5 and t <= 30:
            enf()
        elif t > 30 and t <= 37.5:
            normal()
        else:
            tf()
        x = x + 1

    except ValueError:
        print("Introduzca un valor valido")










