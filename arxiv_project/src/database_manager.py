import sqlite3
class DatabaseManager:
    def __init__(self, db_path):
        try:
            self.conn = sqlite3.connect(db_path)
        except sqlite3.OperationalError as e:
            print(f"Error connecting to database at {db_path}: {e}")
            raise
    
    def save_analysis(self, paper_id, analysis):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO analysis (paper_id, content) VALUES (?, ?)', (paper_id, analysis))
        self.conn.commit()

    def close(self):
        self.conn.close()
