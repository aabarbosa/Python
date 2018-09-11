N = int(raw_input())
list=[]
for n in range(N):
	celcius = float(raw_input())
	list.append(celcius)

for celcius in list:
	print 1.8*celcius + 32