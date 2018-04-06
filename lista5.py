ss = 'hoje a noite'
vogais = 0
consoantes =0

for caracter in ss:
	if caracter in 'aeiou':
		vogais = vogais + 1
	else:
		consoantes = consoantes + 1
print ("vogais: %d" %vogais)
print ("consoantes: %d" %consoantes)
print (len(ss))
