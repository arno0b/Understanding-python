import mysql.connector 

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'arnob12345'
)
#print(mydb.is_connected())

# Create a cursor object
cur = mydb.cursor()

# Execute the SELECT statement to retrieve data from the FSDS1 table
cur.execute('SELECT * FROM fsds_db.FSDS1')

# Loop through the results and print each row
for i in cur:
    print(i)

# Close the cursor and database connection
cur.close()
mydb.close()