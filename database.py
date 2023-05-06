import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('urls.db', check_same_thread=False)
        self.create_table()

    def create_table(self):
        create_sql = """
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                short_url TEXT NOT NULL
            )
        """
        self.conn.execute(create_sql)
        self.conn.commit()

    def insert(self, url, short_url):
        insert_sql = """
            INSERT INTO urls(url, short_url) VALUES (?, ?)
        """
        self.conn.execute(insert_sql, (url, short_url))
        self.conn.commit()

    def get_url(self, short_url):
        select_url = """
            SELECT url FROM urls WHERE short_url = ?
        """
        cursor = self.conn.execute(select_url, (short_url,))
        url = cursor.fetchone()
        return url[0] if url else None
