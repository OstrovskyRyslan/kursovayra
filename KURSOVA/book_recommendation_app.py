import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from database_connection import add_book_to_db, get_recommendations_from_db  # Импортируем функции

# Функция для добавления книги
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    genre = entry_genre.get()
    year = entry_year.get()
    rating = entry_rating.get()

    if title and author and genre and year and rating:
        try:
            add_book_to_db(title, author, genre, int(year), float(rating))  # Используем функцию из файла
            messagebox.showinfo("Успіх", "Книга додана до бази даних.")
        except Exception as e:
            messagebox.showerror("Помилка", f"Сталася помилка: {e}")
    else:
        messagebox.showwarning("Увага", "Будь ласка, заповніть всі поля.")

# Функция для рекомендаций
def recommend_books():
    genre = combo_genre.get()
    min_rating = entry_recommend_rating.get()

    try:
        # Получаем книги из базы данных, отфильтрованные по жанру и минимальному рейтингу
        books = get_recommendations_from_db(genre, float(min_rating) if min_rating else None)  

        result_text.delete(1.0, tk.END)
        if books:
            result_text.insert(tk.END, "Рекомендовані книги:\n\n")
            for book in books:
                result_text.insert(tk.END, f"{book.Title} by {book.Author} ({book.Year}) - Rating: {book.Rating}\n")
        else:
            result_text.insert(tk.END, "Немає книг, що відповідають критеріям.\n")
    except Exception as e:
        messagebox.showerror("Помилка", f"Сталася помилка: {e}")

# Создание главного окна
root = tk.Tk()
root.title("Програмний додаток для рекомендацій книг")
root.geometry("600x600")
root.config(bg="#e0f7fa")  # Задаем цвет фона главного окна

# Стиль для виджетов
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 12),
                padding=10,
                relief="flat",
                background="#4CAF50",  # Зеленый цвет кнопки
                foreground="red")  # Красный текст на кнопке
style.map("TButton",
          background=[('active', '#388E3C')])  # Меняется цвет при наведении (темно-зеленый)

# Ввод данных для добавления книги
frame_add_book = tk.LabelFrame(root, text="Додати книгу", padx=10, pady=10, bg="#e0f7fa", font=("Arial", 14))
frame_add_book.pack(padx=10, pady=10, fill="both")

tk.Label(frame_add_book, text="Назва книги:", bg="#e0f7fa", font=("Arial", 12)).grid(row=0, column=0)
entry_title = tk.Entry(frame_add_book, font=("Arial", 12), bg="#ffffff")
entry_title.grid(row=0, column=1)

tk.Label(frame_add_book, text="Автор:", bg="#e0f7fa", font=("Arial", 12)).grid(row=1, column=0)
entry_author = tk.Entry(frame_add_book, font=("Arial", 12), bg="#ffffff")
entry_author.grid(row=1, column=1)

tk.Label(frame_add_book, text="Жанр:", bg="#e0f7fa", font=("Arial", 12)).grid(row=2, column=0)
entry_genre = tk.Entry(frame_add_book, font=("Arial", 12), bg="#ffffff")
entry_genre.grid(row=2, column=1)

tk.Label(frame_add_book, text="Рік видання:", bg="#e0f7fa", font=("Arial", 12)).grid(row=3, column=0)
entry_year = tk.Entry(frame_add_book, font=("Arial", 12), bg="#ffffff")
entry_year.grid(row=3, column=1)

tk.Label(frame_add_book, text="Рейтинг:", bg="#e0f7fa", font=("Arial", 12)).grid(row=4, column=0)
entry_rating = tk.Entry(frame_add_book, font=("Arial", 12), bg="#ffffff")
entry_rating.grid(row=4, column=1)

# Используем ttk.Button вместо tk.Button
ttk.Button(frame_add_book, text="Додати книгу", command=add_book, style="TButton").grid(row=5, columnspan=2, pady=10)

# Ввод данных для получения рекомендаций
frame_recommend = tk.LabelFrame(root, text="Рекомендації", padx=10, pady=10, bg="#e0f7fa", font=("Arial", 14))
frame_recommend.pack(padx=10, pady=10, fill="both")

tk.Label(frame_recommend, text="Жанр для рекомендацій:", bg="#e0f7fa", font=("Arial", 12)).grid(row=0, column=0)

# Добавляем ComboBox для выбора жанра
combo_genre = ttk.Combobox(frame_recommend, font=("Arial", 12), values=["Фантастика", "Детектив", "Роман", "Біографія"])  # Добавьте список жанров
combo_genre.grid(row=0, column=1)

tk.Label(frame_recommend, text="Мінімальний рейтинг:", bg="#e0f7fa", font=("Arial", 12)).grid(row=1, column=0)
entry_recommend_rating = tk.Entry(frame_recommend, font=("Arial", 12), bg="#ffffff")
entry_recommend_rating.grid(row=1, column=1)

# Добавление кнопки для получения рекомендаций
ttk.Button(frame_recommend, text="Отримати рекомендації", command=recommend_books, style="TButton").grid(row=2, columnspan=2, pady=10)

# Місце для виведення результатов рекомендаций
result_text = tk.Text(root, height=10, width=50, font=("Arial", 12), bg="#ffffff", wrap=tk.WORD)
result_text.pack(padx=10, pady=10)

# Запуск основного цикла
root.mainloop()