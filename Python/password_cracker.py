pswd = input("Your Password:")
l = len(pswd)
x=0
y=0
le = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
g="a"

while (x in range(len(le)) and (g!=pswd)):
    g1 = le[x]
    x = x+1
    y=0
    while (y in range(len(le)) and (g!=pswd)):
        g2 = g1 + le[y]
        y=y+1
        z=0
        while (z in range(len(le)) and (g!=pswd)):
            g3 = g2 + le[z]
            z=z+1

       
print ("your password is:", g)