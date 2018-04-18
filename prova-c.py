import psycopg2

conn = psycopg2.connect("dbname=ifrn user=postgres host=localhost")
cur = conn.cursor()
cur.execute("SELECT * FROM aluno ORDER BY nome;")

rows = cur.fetchall()

for row in rows:
	print()
	print('Matricula:',row[1])
	print('ndisplina:',row[2])
	print('nota01:',row[3])
	print('nota02:',row[4])
	media = int(row[3]*2+row[4])/5
	print ('media e: '%d , media)
print()
cur.close()
conn.close()
