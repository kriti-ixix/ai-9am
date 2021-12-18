import mysql.connector
import pandas as pd

connection = mysql.connector.connect(host='localhost', user='root',
passwd='', database='demo')

cursor = connection.cursor()

insert_query = "insert into students values(4, 'New Student', 'F', 60)"
cursor.execute(insert_query)
connection.commit()
print("Values inserted")

update_query = "update students set marks=55 where rollno=4"
cursor.execute(update_query)
connection.commit()
print("Values updated")

delete_query = "delete from students where rollno=4"
cursor.execute(delete_query)
connection.commit()
print("Values deleted")

df = pd.read_sql("select * from students", connection)
print(df)