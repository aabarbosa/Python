# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 154

def professores(alocacao, disciplina):
	list_prof = alocacao.get(disciplina, 0)
	
	if type(list_prof) == list:
		return len(list_prof)
	else:
		return list_prof			


alocacao = {"P1": ['Jorge', 'Dalton','Wilkerson'],
         "IC": ['Andrey', 'Joseana'],
         "P2": ['Livia', 'Raquel', 'Nazareno'],
         "LPT": ['Marli']}

print professores(alocacao, "P1")
print professores(alocacao, "IC")
print professores(alocacao, "P1")
print professores(alocacao, "ICcc")

