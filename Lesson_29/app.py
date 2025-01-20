import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="mydb",
        user="postgres",
        password="password",
        host="my-postgres",
        port=5432
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50)
        );
    """)
    conn.commit()
    conn.close()

def test_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO test_table (name) VALUES ('Test User');")
    conn.commit()
    cursor.execute("SELECT * FROM test_table;")
    print("Records:", cursor.fetchall())
    conn.close()

if __name__ == "__main__":
    create_table()
    test_database()