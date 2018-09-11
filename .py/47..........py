# 0, 1, 3, 7, 15…, 1023
#   +1 +2 +4 +8

razao = 1

for i in range(0, 1024):

	print i + razao

	razao = razao*2