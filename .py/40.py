# coding: utf-8

N = int(raw_input())
assert N>=1

list = []
list_aprovados = []
list_reprovados = []

for alunos in range(N):
	nota = float(raw_input())
	list.append(nota)
	
soma_notas_aprovados = 0
soma_notas_reprovados = 0
	
for nota_num_aluno in range(N):
	if list[nota_num_aluno] >=7:
		list_aprovados.append(list[nota_num_aluno])
		soma_notas_aprovados += list[nota_num_aluno]
	else:
		list_reprovados.append(list[nota_num_aluno])
		soma_notas_reprovados += list[nota_num_aluno]
		
print 'Reprovados: %d' % len(list_reprovados)

if len(list_reprovados) > 0:
	print 'Média: %.1f' % (soma_notas_reprovados/len(list_reprovados)) + '\n'
else:
	print

print 'Aprovados: %d' % len(list_aprovados)
if len(list_aprovados) > 0:
	print 'Média: %.1f' % (soma_notas_aprovados/len(list_aprovados))

