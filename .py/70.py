# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 70

def aluno_top(nomes_alunos, nums_exerc):
	'''	 Encontra máximo na lista nums_exerc que corresponde ao maior
	número de resoluções feitas por um determinado aluno  '''
	
	indice_aluno = 0
	maior_nresolucoes = nums_exerc[0]
	for i in range(len(nomes_alunos)):
		
		if nums_exerc[i] > maior_nresolucoes:
			maior_nresolucoes = nums_exerc[i]
			indice_aluno = i
			
	return nomes_alunos[indice_aluno], maior_nresolucoes
		
	
nums_exerc = map(int, raw_input().split())
nomes_alunos = map(str, raw_input().split())

aluno,num_qst = aluno_top(nomes_alunos, nums_exerc)
print aluno, num_qst
