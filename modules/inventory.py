import sqlite3
from datetime import datetime

DB_PATH = "data/smartfridge.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_items(items):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    for item in items:
        cursor.execute("INSERT INTO inventory (item_name, timestamp) VALUES (?, ?)", (item, now))
    conn.commit()
    conn.close()

def get_latest_items():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT item_name FROM inventory ORDER BY id DESC LIMIT 33")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]
