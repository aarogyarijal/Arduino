eq=input("Any Equation:")
s="!2*8/4+7!"
s="!"+eq+"!"
loop=0


while loop != 4:
	#Divide
	a=0 #Variable to see if end of equation is reached
	f=1 #Variable to store position of operator and check if operater is reached
	b=1
	dr=0 #Counter to see if all digits before the digit to be replaced is reached
	nonif=0 #Counter to find non in front of operator
	nonib=0 #Counter to find non in behind of operator
	bdc1=0
	bdc2=0 #Counter used while taking out Big Digit
	bdif=0 #Big Digit infront
	bdib=0 #
	drs=""


	l=len(s)

	while a != (l-1):
		d=s[a]
		

		if d == "/":
			f=a-1
			while s[f]!="+" and s[f]!="-" and s[f]!="*" and s[f]!="/" and s[f]!="!":
				nonif=nonif+1
				f=f-1
	
			while bdc1 != nonif:
				bdif = float(s[a-nonif:a])
				bdc1 =bdc1+1
			d1=bdif
				
			b=a+1
			while s[b]!="+" and s[b]!="-" and s[b]!="*" and s[b]!="/" and s[b]!="!":
				nonib=nonib+1
				b=b+1
	
			while bdc2 != nonib:
				bdib= float(s[a+1:a+nonib+1])
				bdc2 =bdc2+1
	
			
			d2=bdib
			d=d1/d2
			
	
			while dr != (a-nonif):
				drs=drs + s[dr]
				dr=dr+1
			s=drs+str(d)+s[a+nonib+1:l-1]+"!"	
			a=a-nonif-1
			l=(l-(nonif+nonib+1))
		a=a+1
		
	
	
	
	
	
	#Multiply
	a=0 #Variable to see if end of equation is reached
	f=1 #Variable to store position of operator and check if operater is reached
	b=1
	dr=0 #Counter to see if all digits before the digit to be replaced is reached
	nonif=0 #Counter to find non in front of operator
	nonib=0 #Counter to find non in behind of operator
	bdc1=0
	bdc2=0 #Counter used while taking out Big Digit
	bdif=0 #Big Digit infront
	bdib=0 #	
	drs=""	
	
	
	l=len(s)	
	
	while a != (l-1):
		d=s[a]
		
		if d == "*":
			f=a-1
			while s[f]!="+" and s[f]!="-" and s[f]!="*" and s[f]!="/" and s[f]!="!":
				nonif=nonif+1
				f=f-1
		
			while bdc1 != nonif:
				bdif = float(s[a-nonif:a])
				bdc1 =bdc1+1
			d1=bdif
				
			b=a+1
			while s[b]!="+" and s[b]!="-" and s[b]!="*" and s[b]!="/" and s[b]!="!":
				nonib=nonib+1
				b=b+1
	
			while bdc2 != nonib:
				bdib= float(s[a+1:a+nonib+1])
				bdc2 =bdc2+1		
	
			
			d2=bdib
			d=d1*d2
	
			while dr != (a-nonif):
				drs=drs + s[dr]
				dr=dr+1
			s=drs+str(d)+s[a+nonib+1:l-1]+"!"	
			a=a-nonif-1
			l=(l-(nonif+nonib+1))
		a=a+1		



	
	
	
	#Add
	a=0 #Variable to see if end of equation is reached
	f=1 #Variable to store position of operator and check if operater is reached
	b=1
	dr=0 #Counter to see if all digits before the digit to be replaced is reached
	nonif=0 #Counter to find non in front of operator
	nonib=0 #Counter to find non in behind of operator
	bdc1=0
	bdc2=0 #Counter used while taking out Big Digit
	bdif=0 #Big Digit infront
	bdib=0 #
	drs=""
	
	
	l=len(s)
	
	while a != (l-1):
		d=s[a]
	
		if d == "+":
			f=a-1
			while s[f]!="+" and s[f]!="-" and s[f]!="*" and s[f]!="/" and s[f]!="!":
				nonif=nonif+1
				f=f-1
	
			while bdc1 != nonif:
				bdif = float(s[a-nonif:a])
				bdc1 =bdc1+1
			if str(s[a-nonif-1])=="-":
				d1=0-bdif
			else:
				d1=bdif
				
			b=a+1
			while s[b]!="+" and s[b]!="-" and s[b]!="*" and s[b]!="/" and s[b]!="!":
				nonib=nonib+1
				b=b+1
	
			while bdc2 != nonib:
				bdib= float(s[a+1:a+nonib+1])
				bdc2 =bdc2+1
	
			
			d2=bdib
			d=d1+d2
			if d<0:
				d=-d
	
			while dr != (a-nonif):
				drs=drs + s[dr]
				dr=dr+1	
			s=drs+str(d)+s[a+nonib+1:l-1]+"!"	
			a=a-nonif-1
			l=(l-(nonif+nonib+1))
		a=a+1	



	


	#Subtract
	a=0 #Variable to see if end of equation is reached
	f=1 #Variable to store position of operator and check if operater is reached
	b=1
	dr=0 #Counter to see if all digits before the digit to be replaced is reached
	nonif=0 #Counter to find non in front of operator
	nonib=0 #Counter to find non in behind of operator
	bdc1=0
	bdc2=0 #Counter used while taking out Big Digit
	bdif=0 #Big Digit infront
	bdib=0 #
	drs=""
	
	
	l=len(s)
	
	while a != (l-1):
		d=s[a]
	
		if d == "-":
			f=a-1
			while s[f]!="+" and s[f]!="-" and s[f]!="*" and s[f]!="/" and s[f]!="!":
				nonif=nonif+1
				f=f-1
	
			while bdc1 != nonif:
				bdif = float(s[a-nonif:a])
				bdc1 =bdc1+1
			d1=bdif
				
			b=a+1
			while s[b]!="+" and s[b]!="-" and s[b]!="*" and s[b]!="/" and s[b]!="!":
				nonib=nonib+1
				b=b+1
	
			while bdc2 != nonib:
				bdib= float(s[a+1:a+nonib+1])
				
				bdc2 =bdc2+1
	
			
			d2=bdib
			d=d1-d2
	
			while dr != (a-nonif):
				drs=drs + s[dr]
				dr=dr+1
			s=drs+str(d)+s[a+nonib+1:l-1]+"!"	
			a=a-nonif-1
			l=(l-(nonif+nonib+1))
		a=a+1
	
	op=s[1:len(s)-1]
	
	loop=loop+1
print(op)
	
			