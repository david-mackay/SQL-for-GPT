import mysql.connector

def get_db_schema(host, user, password, database):
    conn = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    schema_info = {}
    for table in tables:
        table_name = (
            table[0].decode("utf-8") if isinstance(table[0], bytes) else table[0]
        )
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        column_info = [
            {
                "name": col[0].decode("utf-8") if isinstance(col[0], bytes) else col[0],
                "type": col[1],
            }
            for col in columns
        ]
        schema_info[table_name] = column_info
    conn.close()
    return f"database name: {database}, tables: {str(schema_info)}"
