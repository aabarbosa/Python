# coding: utf-8

word = raw_input()
list_vogais = ['a','e', 'i', 'o', 'u']

# Verificação: se contém vogais na variável word.
# Imprima a primeira vogal encontrada.
# Se encontrar, pare a iteração.
for i in range(len(word)):
	if word[i].lower() in list_vogais:
		print word[i]  
		break

# Verificação: se não contém vogais na variável word imprima '-'.
if word[i].lower() not in list_vogais:
	print '-'
