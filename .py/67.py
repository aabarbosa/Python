# coding: utf-8

CPF = raw_input()
soma1 = 0
soma2 = 0
n = 1

# Estrutura de soma para cálculo do Dígito Verificador 1 (dig1)
for i in range(2,11):
	soma1 += i * int(CPF[len(CPF) - n])
	n += 1
	
dig1 = (soma1*10) % 11
CPF += str(dig1)

n = 1

# Estrutura de soma para cálculo do Dígito Verificador 2 (dig2)
for i in range(2,12):
	soma2 += 1 * int(CPF[len(CPF) - n])
	n += 1

dig2 = (soma2*10) % 11

print str(dig1) + str(dig2)