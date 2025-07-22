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
