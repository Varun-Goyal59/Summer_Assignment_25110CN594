import mysql.connector

connection = mysql.connector.connect(
    user='your_username',
    password='your_password',
    host='your_host',
    database='your_database'
)
cursor = connection.cursor()

query = "SELECT * FROM your_table_name"
cursor.execute(query)

print("Using fetchall():")
all_records = cursor.fetchall()
for record in all_records:
    print(record)

cursor.execute(query)

print("\nUsing fetchone():")
record_one = cursor.fetchone()
print(record_one)

cursor.execute(query)

print("\nUsing fetchmany():")
n=int(input("Enter no. of record to fetch: "))
records_many = cursor.fetchmany(3)
for record in records_many:
    print(record)

print("\nTotal row count (using rowcount):")
print(cursor.rowcount)

cursor.close()
connection.close()