import time

pswd = input("Your Password:")
start = time.time()
l = len(pswd)
attempt=0
a=0
b=0
c=0
d=0
e=0
f=0
ga=0
h=0
i=0
le = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
g=""

while g != pswd:
	if l == 9:
		g=""
		g1=le[a]
		g=g+g1
		g2=le[b]
		g=g+g2
		g3=le[c]
		g=g+g3
		g4=le[d]
		g=g+g4
		g5=le[e]
		g=g+g5
		g6=le[f]
		g=g+g6
		g7=le[ga]
		g=g+g7
		g8=le[h]
		g=g+g8
		g9=le[i]
		g=g+g9
		a=a+1
		if a == 36:
			a=0
			b=b+1
		
		if b == 36:
			b=0
			c=c+1
		if c == 36:
			c=0
			d=d+1
		if d == 36:
			d=0
			e=e+1
		if e == 36:
			e=0
			f=f+1
		if f == 36:
			f=0
			g=g+1
		if ga == 36:
			ga=0
			h=h+1
		if h == 36:
			h=0
			i=i+1
		print (g)
		attempt=attempt+1

	if l == 8:
		g=""
		g1=le[a]
		g=g+g1
		g2=le[b]
		g=g+g2
		g3=le[c]
		g=g+g3
		g4=le[d]
		g=g+g4
		g5=le[e]
		g=g+g5
		g6=le[f]
		g=g+g6
		g7=le[ga]
		g=g+g7
		g8=le[h]
		g=g+g8
		a=a+1
		if a == 36:
			a=0
			b=b+1
		
		if b == 36:
			b=0
			c=c+1
		if c == 36:
			c=0
			d=d+1
		
		if d == 36:
			d=0
			e=e+1

		if e == 36:
			e=0
			f=f+1
		if f == 36:
			f=0
			g=g+1
		if ga == 36:
			ga=0
			h=h+1
		print (g)
		attempt=attempt+1

	if l == 7:
		g=""
		g1=le[a]
		g=g+g1
		g2=le[b]
		g=g+g2
		g3=le[c]
		g=g+g3
		g4=le[d]
		g=g+g4
		g5=le[e]
		g=g+g5
		g6=le[f]
		g=g+g6
		g7=le[ga]
		g=g+g7
		a=a+1
		if a == 36:
			a=0
			b=b+1
		
		if b == 36:
			b=0
			c=c+1
		if c == 36:
			c=0
			d=d+1
		if d == 36:
			d=0
			e=e+1
		if e == 36:
			e=0
			f=f+1
		if f == 36:
			f=0
			ga=ga+1
		print (g)
		attempt=attempt+1


	if l == 6:
		g=""
		g1=le[a]
		g=g+g1
		g2=le[b]
		g=g+g2
		g3=le[c]
		g=g+g3
		g4=le[d]
		g=g+g4
		g5=le[e]
		g=g+g5
		g6=le[f]
		g=g+g6
		a=a+1
		if a == 36:
			a=0
			b=b+1
		
		if b == 36:
			b=0
			c=c+1
		if c == 36:
			c=0
			d=d+1
		if d == 36:
			d=0
			e=e+1
		if e == 36:
			e=0
			f=f+1
		print (g)
		attempt=attempt+1



	if l == 5:
		g=""
		g1=le[a]
		g=g+g1
		g2=le[b]
		g=g+g2
		g3=le[c]
		g=g+g3
		g4=le[d]
		g=g+g4
		g5=le[e]
		g=g+g5
		a=a+1

		if a == 36:
			a=0
			b=b+1
		
		if b == 36:
			b=0
			c=c+1
		if c == 36:
			c=0
			d=d+1
		if d == 36:
			d=0
			e=e+1
		print (g)
		attempt=attempt+1


	if l == 4:
		g=""
		g1=le[a]
		g=g+g1
		g2=le[b]
		g=g+g2
		g3=le[c]
		g=g+g3
		g4=le[d]
		g=g+g4
		a=a+1


		if a == 36:
			a=0
			b=b+1
		
		if b == 36:
			b=0
			c=c+1

		if c == 36:
			c=0
			d=d+1
		print (g)
		attempt=attempt+1


	if l == 3:
		g=""
		g1=le[a]
		g=g+g1
		g2=le[b]
		g=g+g2
		g3=le[c]
		g=g+g3
		a=a+1


		if a == 36:
			a=0
			b=b+1
		
		if b == 36:
			b=0
			c=c+1
		print (g)
		attempt=attempt+1


	if l == 2:
		g=""
		g1=le[a]
		g=g+g1
		g2=le[b]
		g=g+g2

		a=a+1


		if a == 36:
			a=0
			b=b+1
		print (g)
		attempt=attempt+1


	if l == 1:
		g=""
		g1=le[a]
		g=g+g1
		a=a+1
		print (g)
		attempt=attempt+1


end = time.time()
print ("Your password is:", g)
print("Time taken:", end - start)
print ("Attempts:", attempt)