palavra = raw_input()

for car in palavra:
	if car=='a' or car=='e' or car=='i' or car=='o' or car=='u' or car=='A' or car=='E' or car=='I' or car=='O' or car=='U':
		print '<%s>' % car + ' sim'
	else:
		print '<%s>' % car + ' nao'