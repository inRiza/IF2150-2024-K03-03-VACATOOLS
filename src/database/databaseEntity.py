from pathlib import Path
import sqlite3


class DatabaseEntity:
    def __init__(self, db_path: str = None):
        if db_path is None:
            # Jika path tidak diberikan, gunakan path relatif ke lokasi file ini
            db_path = Path(__file__).parent / 'database.db'
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, isolation_level=None)  # Auto-commit aktif
        self.cursor = self.conn.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        """Ensure all tables exist."""
        # Journal Log Table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS JOURNAL_LOG (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            country TEXT NOT NULL,
            city TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        );""")

        # Bucket List Table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS BUCKET_LIST (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            country TEXT NOT NULL,
            city TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (id) REFERENCES journal_log (id)
        );""")

        # Statistics Table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS STATISTIC (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            country TEXT NOT NULL,
            city TEXT NOT NULL,
            count INTEGER NOT NULL,
            FOREIGN KEY (id) REFERENCES journal_log (id)
        );""")
        
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS LOCATION (
            country TEXT NOT NULL,
            city TEXT NOT NULL
        );""")

    def addData(self, namaTabel: str, **data):
        # Cek apakah data sudah ada berdasarkan title, country, dan city
        if 'title' in data and 'country' in data and 'city' in data:
            query = f"""
            SELECT COUNT(*) FROM {namaTabel} 
            WHERE title = ? AND country = ? AND city = ?
            """
            self.cursor.execute(query, (data['title'], data['country'], data['city']))
            count = self.cursor.fetchone()[0]
            if count > 0:
                print(f"Data dengan title '{data['title']}', country '{data['country']}', dan city '{data['city']}' sudah ada.")
                return  # Data sudah ada, tidak perlu ditambahkan lagi
        
        # Lanjutkan menambahkan data jika belum ada
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        query = f"INSERT INTO {namaTabel} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()  # Pastikan perubahan disimpan
        print(f"Data berhasil ditambahkan ke {namaTabel}")



    def getData(self, namaTabel: str, *kolom):
        query = f"SELECT {', '.join(kolom) if kolom else '*'} FROM {namaTabel}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        return [dict(zip(columns, row)) for row in rows]

    def executeQuery(self, query: str):
        """
        Menjalankan query SQL mentah.
        :param query: Query SQL sebagai string.
        :return: Hasil dari query.
        """
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None
            print("Database connection successfully disconnected.")
