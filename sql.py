import pymysql as sql
import sys

connect = sql.connect(
	host='localhost',
	port=3306,
	user='root',
	password='123456',
	database='account'
)

id = sys.argv[1]
name = sys.argv[2]
string = "insert into account values(%s,'%s')" %(id,name)
print(string)

cursor = connect.cursor()
value = cursor.execute(string)
connect.commit()

print("MSG: " + str(value))

string = "select * from account";
cursor.execute(string)
rows = cursor.fetchall()

for i in rows:
	print(i[0], "\t", i[1])
