import psycopg2

db_params = {
    'host': 'localhost',    # Replace with your database host
    'database': 'crm',
    'user': 'eator',
    'password': '123456'
}

# Establish a database connection
try:
    connection = psycopg2.connect(**db_params)

    # Create a cursor
    cursor = connection.cursor()

    # Now you can execute SQL queries using the cursor
    # For example:
    cursor.execute("SELECT * FROM test")

    # Fetch the results (if needed)
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    connection.close()

except psycopg2.Error as error:
    print("Error connecting to PostgreSQL:", error)
