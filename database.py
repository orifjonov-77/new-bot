import sqlite3
from datetime import datetime, timedelta

DB_NAME = "study_space.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            balance INTEGER DEFAULT 0,
            is_vip BOOLEAN DEFAULT 0,
            vip_until DATETIME
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            description TEXT,
            price INTEGER DEFAULT 10000,
            file_id TEXT,
            image_id TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def add_user(telegram_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO users (telegram_id) VALUES (?)', (telegram_id,))
    conn.commit()
    conn.close()

def get_user(telegram_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE telegram_id = ?', (telegram_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def set_vip(telegram_id, days=30):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    vip_until = datetime.now() + timedelta(days=days)
    cursor.execute('UPDATE users SET is_vip = 1, vip_until = ? WHERE telegram_id = ?', 
                   (vip_until.strftime('%Y-%m-%d %H:%M:%S'), telegram_id))
    conn.commit()
    conn.close()

def check_vip(telegram_id):
    user = get_user(telegram_id)
    if user and user[2]:  # is_vip
        vip_until = datetime.strptime(user[3], '%Y-%m-%d %H:%M:%S')
        if vip_until > datetime.now():
            return True
        else:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET is_vip = 0, vip_until = NULL WHERE telegram_id = ?', (telegram_id,))
            conn.commit()
            conn.close()
    return False

def add_file(name, category, description, price, file_id, image_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO files (name, category, description, price, file_id, image_id) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, category, description, price, file_id, image_id))
    conn.commit()
    conn.close()

def get_files_by_category(category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM files WHERE category = ?', (category,))
    files = cursor.fetchall()
    conn.close()
    return files

def get_file(file_id_db):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM files WHERE id = ?', (file_id_db,))
    file = cursor.fetchone()
    conn.close()
    return file

if __name__ == '__main__':
    init_db()
