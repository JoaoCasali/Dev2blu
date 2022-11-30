import psycopg2

try:
    conn = psycopg2.connect(host = 'localhost', port = "5432", user = "moredev", password = "123456", database = "postgres" )
    print("deu certo")
except:
    print("deu merda")

cursor = conn.cursor()
cursor.execute("""
create table conta(
	id int primary key generated always as identity,
	numero varchar(200) not null,
	agencia varchar(14) not null
)
""")

cursor.execute("insert into conta values (default, 521, 'joao')")

cursor.close()
conn.commit()

conn.close()
