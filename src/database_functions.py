import psycopg2 as pg2
import database_info

def connect_database():
    conn = pg2.connect(database=database_info.database, user=database_info.username,password=database_info.password, host=database_info.host, port=database_info.port)
    conn.close()

connect_database() 
