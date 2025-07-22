import pyodbc

def connect_to_sql():
    server = 'DESKTOP-DFDNFD1\\SQLEXPRESS'
    database = 'MyDatabase'
    username = 'py_conn'
    password = '123'

    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    )
    return conn

print("inserting data...")
def load_data(df):
    conn = connect_to_sql()
    cursor = conn.cursor()


     # Check if table exists first to avoid error when truncating non-existent table
    cursor.execute("IF OBJECT_ID('users', 'U') IS NOT NULL TRUNCATE TABLE users")
    conn.commit()
    print('TRUNCATE TABLE.....') 

    create_table_query = """
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='users' AND xtype='U')
    CREATE TABLE users (
        user_id INT NOT NULL,
        product_id INT,
        price FLOAT
    )
    """
    cursor.execute(create_table_query)
    conn.commit()

    insert_query = "INSERT INTO users (user_id, product_id, price) VALUES (?, ?, ?)"
    for _, row in df.iterrows():
        cursor.execute(insert_query, row['user_id'], row['product_id'], row['price'])

    conn.commit()
    conn.close()
    print("Data loaded successfully.")
