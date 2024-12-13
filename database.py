import sqlite3

def initialize_database(db_name="qa_database.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS qa_pairs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_question_answer(question, answer, db_name="qa_database.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO qa_pairs (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

def fetch_last_qa(db_name="qa_database.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM qa_pairs ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0], result[1]
    return None, None
