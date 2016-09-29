x=1
while x==1:
    a = input()

    if a.isupper() == True:
        print("Chilea")
    elif a.endswith("?") == True or a.startswith("¿"):
        print("Ofi")
    elif len(a) == 0:
        print("Mmm")
    else:
        print("Me da igual")


