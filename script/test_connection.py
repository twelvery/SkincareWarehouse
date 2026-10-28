import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

db_url = os.getenv("DATABASE_URL")
if not db_url:
    print("Error : URL database tidak ditemukan. Cek file .env Anda.")
    exit()
     
engine = create_engine(db_url)

with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    print("Koneksi ke database berhasil. Hasil query:", result.fetchone()[0])