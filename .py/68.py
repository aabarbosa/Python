# coding: utf-8

NC_DV = map(str, raw_input().split())
NC = NC_DV[0]
DV = NC_DV[1]
somatorio = 0

# Somatório de todos os números da Conta
for i in range(len(NC)):
	somatorio += int(NC[i])

# Verificação de Conta válida ou não
if somatorio % 11 == int(DV):
	print 'ok'
else:
	print 'erro'