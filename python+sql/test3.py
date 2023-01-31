import mysql.connector 
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'arnob12345'
)
print(mydb.is_connected())

cur = mydb.cursor()
#cur.execute('CREATE DATABASE test_db')
cur.execute("CREATE TABLE test_db.test_table(idx INT, RI FLOAT, Na FLOAT, Mg FLOAT, Al FLOAT, Si FLOAT,K FLOAT,Ca FLOAT,Ba FLOAT,Fe FLOAT,Class INT)")
cur.execute('INSERT INTO test_db.test_table VALUES)