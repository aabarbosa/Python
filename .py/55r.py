# coding: utf-8
 
list_values = map(int, raw_input().split())
assert len(list_values) >= 2
 
maior_numero = 0
segundo_maior = 0
 
for value in list_values:       
        if value > segundo_maior:                
                segundo_maior = value
        if value > maior_numero:
                segundo_maior = maior_numero
                maior_numero = value
 
print maior_numero + segundo_maior