# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 76 

CPF = raw_input()

# Estrutura de soma para cálculo do Dígito Verificador 1 (dig1)
n = 1
soma1 = 0
for i in range(2,11):
	soma1 += i * int(CPF[len(CPF) - n])
	n += 1
dig1 = (soma1*10)%11
if dig1 == 10:
	dig1 = 0

CPF = str(dig1) + CPF 
print CPF


# Estrutura de soma para cálculo do Dígito Verificador 2 (dig2)
soma2 = 0
n = 1 
for i in range(2,12): 
	soma2 += i * int(CPF[len(CPF) - n])
	n += 1 
dig2 = (soma2*10)%11 
if dig2 == 10:
	dig2 = 0
	
print str(dig1) + str(dig2)