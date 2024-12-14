# VACATOOLS

## Overview
**VACATOOLS** is a project developed as part of the IF2150 course.

Vacatools adalah perangkat lunak yang dirancang untuk membantu pengguna dalam membuat, menyusun, dan mengelola jurnal serta rencana perjalanan. Sistem ini bertujuan untuk meningkatkan efisiensi dalam pengorganisasian informasi terkait perjalanan dan pengalaman pribadi. Dengan menggunakan Vacatools, pengguna dapat mencatat kegiatan harian, menyimpan catatan penting, serta merancang rencana perjalanan dengan lebih mudah dan terstruktur.

## Anggota - VACATOOLS
| NIM  | NAMA |
| ------------- | ------------- |
| 13523127 | Boye Mangaratua Ginting  |
| 13523129 | Ivant Samuel Silaban  |
| 13523133 | Rafa Abdussalam Danadyaksa  |
| 13523144 | Muhamad Nazih Najmudin   |
| 13523164 | Muhammad Rizain Firdaus  |

## Getting Started

### Prerequisites
Make sure you have **Python 3.x** installed on your machine.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/inRiza/IF2150-K03-03-VACATOOLS.git
2. **Navigate to the project directory**:
    ```bash
    cd IF2150-K03-03-VACATOOLS
3. **Install dependencies (if any, e.g., using a requirements.txt file)**:
     ```bash
    pip install -r requirements.txt
4. **Run the main.py**:
   ```python
   python main.py

## Daftar Modul
| NAMA Modul | Pembagian Tugas | 
| ------------- | ------------- |
| DatabaseStatisticController | Boye Mangaratua Ginting  | 
| DatabaseJournalController | Ivant Samuel Silaban  |
| JournalEntity | Ivant Samuel Silaban  |
| BucketEntity | Rafa Abdussalam Danadyaksa  |
| BucketEntity | Rafa Abdussalam Danadyaksa  |
| DatabaseEntity | Muhamad Nazih Najmudin   |
| DatabaseJournalController | Muhamad Nazih Najmudin   |
| formJournalpage | Muhammad Rizain Firdaus  | 
| formbBucketpage | Muhammad Rizain Firdaus  |

## Tabel Journal
| Nama Atribut  | Tipe Data | Deskripsi | 
| ------------- | ------------- | ------------- |
| id | INTEGER  | ID unik setiap entri |
| title	TEXT | TEXT  | Judul aktivitas atau tujuan |
| country | TEXT  | Negara tujuan |
| city | TEXT   | Kota tujuan |
| date | DATE   | Tanggal entri jurnal dibuat |
| description | TEXT  | Penjelasan tujuan atau aktivitas | 

## Tabel Bucket List
| Nama Atribut  | Tipe Data | Deskripsi | 
| ------------- | ------------- | ------------- |
| id | INTEGER  | ID unik setiap entri |
| title	TEXT | TEXT  | Judul aktivitas atau tujuan |
| country | TEXT  | Negara tujuan |
| city | TEXT   | Kota tujuan |
| description | TEXT  | Penjelasan tujuan atau aktivitas | 

## Tabel Statistic
| Nama Atribut  | Tipe Data | Deskripsi | 
| ------------- | ------------- | ------------- |
| id | INTEGER  | ID unik setiap entri |
| country | TEXT  | Negara tujuan |
| city | TEXT   | Kota tujuan |
| count | INTEGER  | Jumlah kunjungan atau entri | 


## Pembagian Tugas
| NIM  | NAMA | Pembagian Tugas | 
| ------------- | ------------- | ------------- |
| 13523127 | Boye Mangaratua Ginting  | Fitur Statistic |
| 13523129 | Ivant Samuel Silaban  | Fitur Journal Log |
| 13523133 | Rafa Abdussalam Danadyaksa  | Fitur Bucket List |
| 13523144 | Muhamad Nazih Najmudin   | Database |
| 13523164 | Muhammad Rizain Firdaus  | User Interface dan Integrasi | 


