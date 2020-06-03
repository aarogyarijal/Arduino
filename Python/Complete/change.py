total = float(input("money:"))
total = total*100

total = int(total)
print (total)
s=0

while total!=0:
	if total >= 25:
		total = total-25
		s=s+1
		print ("update1:", total)
	elif total < 25 and total >= 10:
		total = total-10
		s=s+1
		print ("update1:", total)
	elif total <10 and total >=5:
		total = total - 5
		s=s+1
		print ("update1:", total)
	elif total <5 and total >=1:
		total = total - 1
		s=s+1
		print ("update1:", total)
print(s)