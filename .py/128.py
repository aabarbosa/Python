# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 128

def elimina_menores(list):
	alunos_eliminar = []
	for i in range(len(list)):
		if list[i][1] < 18:
			alunos_eliminar.append(list[i])
			
	for eliminar in alunos_eliminar:
		list.remove(eliminar)
	
	return len(alunos_eliminar)
	
alunos = [ ["pedro",17], ["jose",15], ["maria",18],
           ["manoel",16], ["andre",18] ]
print elimina_menores(alunos)
print alunos

