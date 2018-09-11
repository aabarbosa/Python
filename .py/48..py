
A, B, K = map(int, raw_input().split())

klist = range(1,K+1)
for k in klist:
	if k % A==0 and k % B==0:
		print k
	