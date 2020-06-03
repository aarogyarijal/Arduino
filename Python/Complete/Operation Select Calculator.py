

print('''
1)Add
2)Subtract 
3)Multiply 
4)Divide
''')
a=int(input("(1,2,3,4)?"))
print (a)

if a == 1:
	print("x + y = ans")
	x=int(input("x="))
	y=int(input("y="))
	sum = x+y
	print("The sum is " + str(sum))
if a == 2:
	print("x - y = ans")
	x=int(input("x="))
	y=int(input("y="))
	sum = x-y
	print("The sum is " + str(sum))
if a == 3:
	print("x * y = ans")
	x=int(input("x="))
	y=int(input("y="))
	sum = x*y
	print("The sum is " + str(sum))
if a == 4:
	print("x / y = ans")
	x=int(input("x="))
	y=int(input("y="))
	sum = x/y
	print("The sum is " + str(sum))

 