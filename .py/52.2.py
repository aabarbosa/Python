
n = int(raw_input('n? '))

list_values = []

num1 = 1
num2 = 1

for i in range(n/2 + 1):
	num2 *= num1
	list_values.append(num1)
	list_values.append(num2)
	num1 += 3
	
for i in range(n): 
	print list_values[i]