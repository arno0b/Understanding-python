import mysql.connector 
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'arnob12345'
)
#print(mydb.is_connected())

cur = mydb.cursor()
#cur.execute('SHOW DATABASES')
#for i in cur:
#    print(i)

#cur.execute('CREATE DATABASE FSDS_DB')

cur.execute('USE FSDS_DB')
#cur.execute('CREATE TABLE fsds1 (student_name VARCHAR(500), email_id VARCHAR(500), roll_no INT)')
cur.execute("INSERT INTO fsds1 VALUES('SAKIFARNOB', 'SAKIFARNOB98@GMAIL.COM', 10698)")
mydb.commit()
cur.close()
mydb.close()
