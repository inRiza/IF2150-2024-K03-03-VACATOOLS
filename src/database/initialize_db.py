import sqlite3

def initialize_database():
    # Koneksi ke database (akan membuat database.db jika belum ada)
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Tabel jurnal perjalanan
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS journal_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        judul TEXT NOT NULL,
        nama_negara TEXT NOT NULL,
        nama_kota TEXT NOT NULL,
        tanggal_perjalanan TEXT NOT NULL,
        deskripsi_perjalanan TEXT,
        image_path TEXT
    );
    """)
    
    # Tabel bucket list perjalanan
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bucket_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        judul TEXT NOT NULL,
        nama_negara TEXT NOT NULL,
        nama_kota TEXT NOT NULL,
        deskripsi_perjalanan TEXT
    );          
    """)

    # Tabel statistik negara
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS country_statistics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_negara TEXT UNIQUE NOT NULL,
        jumlah_kunjungan INTEGER DEFAULT 0
    );
    """)

    conn.commit()
    conn.close()

# Jalankan fungsi untuk inisialisasi database
initialize_database()
