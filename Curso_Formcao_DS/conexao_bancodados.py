import psycopg2


conexao = psycopg2.connect(host ='localhost', database='CD', user='postgres', password='cybermen', port=5432)

cursor = conexao.cursor()


consulta = "select * from clientes"

cursor.execute(consulta)

registros = cursor.fetchall()

for row in registros:
    print("Nome = ", row[1])
    print("Estado = ", row[2])
    print("Status = ", row[4])
    print("____________________")
 
cursor.close()
conexao.close()    

