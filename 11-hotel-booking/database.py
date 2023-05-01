import sqlite3


def get_data_from_db(table_name):
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()

    return result
