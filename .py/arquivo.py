import urllib

print "Espere... Baixando resultados"
dados = urllib.urlopen("http://dl.dropbox.com/u/9427789/2012.1/last-results.txt").read().rstrip("\n").split("\n")
print "Resultados baixados\n"

mat = raw_input("Digite sua matricula: ")

print "\nMATRICULA | QUESTAO | N ENVIOS | "+"DATA DE ENVIO".center(19)+" | RESULTADO"
for dado in dados:
   if dado.startswith(mat):
       mat,questao,n_envios,data,result = dado.split(",")
       print " %s | %s | %s | %s | %s" % (mat,questao.center(7),n_envios.center(8),data.center(19),result)