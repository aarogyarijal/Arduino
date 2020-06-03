import time

pswd = input("Your Password:")
start = time.time()
l = len(pswd)
attempt=0
a=0
c=0
le = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
g=""
gs=""

n=0

while gs != pswd:
	char = pswd[c]
	while char != g:
		g=le[a]
		a=a+1
		attempt=attempt+1
	gs=gs+g
	a=0
	c=c+1
	char=""	
	g=""
	print (gs)
	attempt=attempt+1
	

end = time.time()
print ("Your password is:", g)
print("Time taken:", end - start)
print ("Attempts:", attempt)