import pyodbc

# Настройки подключения к базе данных
server = 'DESKTOP-QQAOEK4'
database = 'BooksDB'

conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
    f'Encrypt=yes;'
    f'TrustServerCertificate=yes;'
)

cursor = conn.cursor()

# Функция для добавления книги в базу данных
def add_book_to_db(title, author, genre, year, rating):
    cursor.execute("""
        INSERT INTO Books (Title, Author, Genre, Year, Rating)
        VALUES (?, ?, ?, ?, ?)
    """, (title, author, genre, year, rating))
    conn.commit()

# Функция для получения рекомендаций на основе жанра и рейтинга
def get_recommendations_from_db(genre, min_rating=None):
    query = "SELECT Title, Author, Genre, Year, Rating FROM Books WHERE Genre = ?"
    params = [genre]
    
    if min_rating is not None:
        query += " AND Rating >= ?"
        params.append(min_rating)
    
    cursor.execute(query, params)
    return cursor.fetchall()