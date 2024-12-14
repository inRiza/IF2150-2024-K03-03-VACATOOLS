from databaseEntity import DatabaseEntity

def main():
    # Inisialisasi database
    db = DatabaseEntity()

    # Data dummy untuk tabel STATISTIC
    dummy_statistic_data = [
        {"country": "USA", "city": "New York", "count": 10},
        {"country": "France", "city": "Paris", "count": 5},
        {"country": "Japan", "city": "Tokyo", "count": 8},
        {"country": "Brazil", "city": "Rio de Janeiro", "count": 3},
        {"country": "Australia", "city": "Sydney", "count": 6}
    ]

    # Menambahkan data dummy ke tabel STATISTIC
    for data in dummy_statistic_data:
        try:
            db.addData("STATISTIC", **data)
            print(f"Data berhasil ditambahkan: {data}")
        except Exception as e:
            print(f"Gagal menambahkan data: {data}, Error: {e}")

    # Menampilkan data yang ada di tabel STATISTIC
    print("\nData di tabel STATISTIC:")
    statistics = db.getData("STATISTIC")
    for stat in statistics:
        print(stat)

    # Menutup koneksi database
    db.close()

if __name__ == "__main__":
    main()
