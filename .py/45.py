N = int(raw_input())
assert N >= 0
fatorial = 1

for i in range(N,0,-1):
	fatorial *= i
	
print fatorial