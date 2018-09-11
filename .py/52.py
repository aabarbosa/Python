
n = int(raw_input('n? '))

list_values = []
num1 = 1
num2 = 1

for i in range(n):
	num2 *= num1
	list_values.append(num1)
	list_values.append(num2)
	num1 += 3
	
	print list_values[i]