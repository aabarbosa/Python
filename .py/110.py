# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 110

def fatorial(n):
	fatorial = 1
	for i in range(1,n+1):
		fatorial *= i
	return fatorial
	
def conta_zeros(fatorial):
	fatorial = str(fatorial)
	contador_zeros = 0
	while True:
		for i in range(-1, -len(fatorial), -1):
			if int(fatorial[i]) != 0:
				return contador_zeros
			if int(fatorial[i]) == 0:
				contador_zeros += 1
		return contador_zeros
	
num = int(raw_input())
fatorial_num = fatorial(num)

print conta_zeros(fatorial_num)