import psycopg2
import allure

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

def insert_record():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO test_table (name) VALUES ('Test User');")
    conn.commit()
    conn.close()

def verify_record():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_table WHERE name = 'Test User';")
    result = cursor.fetchall()
    assert len(result) > 0, "No records found with name 'Test User'"
    conn.close()

@allure.feature('Database Operations')
def test_database_operations():
    with allure.step('Create table'):
        create_table()
    with allure.step('Insert record'):
        insert_record()
    with allure.step('Verify record'):
        verify_record()