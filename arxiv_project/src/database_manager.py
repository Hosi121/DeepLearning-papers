import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
    
    def save_analysis(self, paper_id, analysis):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO analysis (paper_id, content) VALUES (?, ?)', (paper_id, analysis))
        self.conn.commit()

    def close(self):
        self.conn.close()
