# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 152

def desempenho(M):
	count = 0
	for i in range(len(M)):
		for j in range(len(M[0])):
			if M[i][j] == 1:
				count += 1
	return count

m1 = [[1, 1, 0, 1],
      [1, 1, 0, 0],
      [1, 1, 1, 0]]

m2 = [[0, 1, 0, 1],
      [1, 1, None, 0],
      [1, None, None, None]]

print desempenho(m1) == 8
print desempenho(m2) == 5

