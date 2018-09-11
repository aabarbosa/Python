# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 78

str_cpf = raw_input()
list_integer_cpf = map(int, list(str_cpf))

CPF_inverted = []
for i in range(-1,-10,-1):
	CPF_inverted.append(list_integer_cpf[i])

# Calcula soma necessária para dígito1
soma1 = 0
for i in range(9):
	soma1 += CPF_inverted[i] * (i+2)
dig1 = (10*soma1)%11
if dig1 == 10:
	dig1 = 0

CPF_inverted.insert(0,dig1)
soma2 = 0
for i in range(10):
	soma2 += CPF_inverted[i] * (i+2)
dig2 = (10*soma2)%11
if dig2 == 10:
	dig2 = 0

print str(dig1) + str(dig2)