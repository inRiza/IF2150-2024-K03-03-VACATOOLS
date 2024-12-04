import sqlite3
from typing import List, Dict

class DatabaseEntity:

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self._initialize_tables()


    def _initialize_tables(self):
        """Ensure required tables exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS daftarTempat (
            nama_negara TEXT PRIMARY KEY,
            jumlah_kunjungan INTEGER
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS journalLog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT,
            nama_negara TEXT,
            nama_kota TEXT,
            tanggal_perjalanan TEXT,
            deskripsi_perjalanan TEXT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS bucketList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT,
            nama_negara TEXT,
            nama_kota TEXT,
            deskripsi TEXT
        )
        """)
        self.conn.commit()


    # Methods for selector
    def addData(self, namaTabel:str, **data):
        # jika data != {}
        if not data == {}:
            # Buat format query
            selected_columns = ", ".join([f"{atribut}" for atribut in data.keys()])
            query = f"INSERT INTO {namaTabel} ({selected_columns}) VALUES ({"?, "*(len(data.keys())-1)}?)"
            
            # Eksekusi query
            self.cursor.execute(query, tuple(data.values()))
            self.conn.commit()
    
    
    def getData(self, namaTabel:str, *kolom, **filter) -> List[dict]:
        # kasus filter = {}
        if filter == {}:
            # kasus kolom = ()
            if kolom == ():
                query = f"SELECT * FROM {namaTabel}"
            else:
                # Buat format query
                selected_columns = ", ".join([f"{atribut}" for atribut in kolom])
                query = f"SELECT {selected_columns} FROM {namaTabel}"
            
            # Eksekusi query
            self.cursor.execute(query)

        # kasus filter != {}
        else:
            filtered_columns = ", ".join([f"{atributFiltered} = ?" for atributFiltered in filter.keys()]) 
            # kasus kolom = ()
            if kolom == ():
                query = f"SELECT * FROM {namaTabel} WHERE {filtered_columns}"
            else:
                # Buat format query
                selected_columns = ", ".join([f"{atribut}" for atribut in kolom])
                query = f"SELECT {selected_columns} FROM {namaTabel} WHERE {filtered_columns}"
            
            # Eksekusi query
            self.cursor.execute(query, tuple(filter.values()))
        
        # Mapping hasil
        rows = self.cursor.fetchall()
        if kolom == ():
            self.cursor.execute(f"PRAGMA table_info({namaTabel})")
            daftar_kolom = [row[1] for row in self.cursor.fetchall()]
        else:
            daftar_kolom = kolom
        # output
        return [dict(zip(daftar_kolom, row)) for row in rows]
               
            
    def setData(self, namaTabel:str, syarat:dict, **data):
        # jika data != {}
        if not data == {}:
            # Buat format query
            selected_columns = ", ".join([f"{atribut} = ?" for atribut in data.keys()])
            syarat_kondisi = " AND ".join([f"{atributSyarat} = ?" for atributSyarat in syarat.keys()])
            values = tuple(data.values()) + tuple(syarat.values())
            query = f"UPDATE {namaTabel} SET {selected_columns} WHERE {syarat_kondisi}"
            
            # Eksekusi query
            self.cursor.execute(query, values)
            self.conn.commit()


    def delData(self, namaTabel:str, **syarat):
        # Buat format query
        syarat_kondisi = " AND ".join([f"{atributSyarat} = ?" for atributSyarat in syarat.keys()])
        query = f"DELETE FROM {namaTabel} WHERE {syarat_kondisi}"
        # Eksekusi query
        self.cursor.execute(query, tuple(syarat.values()))
        self.conn.commit()
        

    # Methods to unconnect
    def close(self):
        """Close the database connection."""
        self.conn.close()