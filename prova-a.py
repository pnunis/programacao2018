import psycopg2

conexao = "dbname=ifrn user=postgres host=localhost"

def cadastro():
    if (ja_tem("aluno")):
        print ("Banco de dados aula")
    else:
        print ("Criando Banco e Tabela de alunos")
        criar_DB()
    matricula = input("Digite a sua matricula: ")
    ndisciplina = input("Digite sua disciplina: ")
    nota1 = input("Digite valor da sua nota 01: ")
    nota2 = input("Digite valor da sua nota 02: ")
    conn = psycopg2.connect(conexao)
    cur = conn.cursor()
    cur.execute("INSERT INTO aluno (matricula, disciplina, nota01, nota2) VALUES (%s, %s, %s, %s)",(matr, nome, camp, area))
    conn.commit()
    cur.close()
    conn.close()
    print("Usuario cadastrado com sucesso!")

def criar_DB():
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    conn = psycopg2.connect("dbname=postgres user=postgres host=localhost")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute('CREATE DATABASE ifrn')
    conn = psycopg2.connect(conexao)
    cur = conn.cursor()
    cur.execute("CREATE TABLE aluno (id serial PRIMARY KEY, matricula text, ndisciplina text, nota1 text, nota2 text);")
    conn.commit()
    conn.close()

def ja_tem(table_str):
    exists = False
    try:
        con = psycopg2.connect(conexao)
        cur = con.cursor()
        cur.execute("select exists(select relname from pg_class where relname='" + table_str + "')")
        exists = cur.fetchone()[0]
        cur.close()
    except psycopg2.Error as e:
        print (e)
    return exists

if __name__ == "__main__": cadastro()
