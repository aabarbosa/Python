# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 109

def autenticacao(senha):
	for i in range(len(senha)-1):
		if (int(senha[i])%2==0 and int(senha[i+1])%2==0) or (int(senha[i])%2==1 and int(senha[i+1])%2==1):
			return 'falso: ' + str(len(senha)) + ' algarismos.'
	return 'verdadeiro: ' + str(len(senha)) + ' algarismos.'
			
senha = raw_input()
print autenticacao(senha)