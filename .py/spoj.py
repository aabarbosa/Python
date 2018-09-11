
N = float(raw_input("diametro "))
A = float(raw_input("altura "))
L = float(raw_input("largura "))
P = float(raw_input("profundidade "))

if (N>=1 and N<=10000) and (L>=1 and L<=10000) and (A>=1 and A<=10000) and (P>=1 and P<=10000):
	if A>=N and L>=N and P>=N:
		print 'S'
	else:
		print 'N'
	