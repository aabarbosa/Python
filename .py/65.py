# coding: utf-8

word = raw_input()
list_vogais = ['a','e', 'i', 'o', 'u']

# Verifica��o: se cont�m vogais na vari�vel word.
# Imprima a primeira vogal encontrada.
# Se encontrar, pare a itera��o.
for i in range(len(word)):
	if word[i].lower() in list_vogais:
		print word[i]  
		break

# Verifica��o: se n�o cont�m vogais na vari�vel word imprima '-'.
if word[i].lower() not in list_vogais:
	print '-'
