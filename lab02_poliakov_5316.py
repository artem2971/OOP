import tkinter as tk
from tkinter import ttk

class FilmLibraryApp:
    """
    Класс «Приложение».
    Реализует графический интерфейс для учета фильмов в фильмотеке.
    """
    def __init__(self, root):
        """Инициализация главного окна приложения."""
        self.root = root
        self.root.title("Фильмотека")
        self.root.geometry("800x500")

    def create_interface(self):
        """
        Метод построения и визуализации экранной формы.
        Создает панель инструментов, таблицу фильмов и панель поиска.
        """
        toolbar = ttk.Frame(self.root, padding=6)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_save = ttk.Button(toolbar, text="Сохранить", command=lambda: None)
        btn_save.pack(side=tk.LEFT, padx=3)
        btn_add = ttk.Button(toolbar, text="Добавить", command=lambda: None)
        btn_add.pack(side=tk.LEFT, padx=3)
        btn_delete = ttk.Button(toolbar, text="Удалить", command=lambda: None)
        btn_delete.pack(side=tk.LEFT, padx=3)
        btn_edit = ttk.Button(toolbar, text="Редактировать", command=lambda: None)
        btn_edit.pack(side=tk.LEFT, padx=3)

        table_frame = ttk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)
        columns = ("film_id", "director", "title", "holder")
        self.films_tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        self.films_tree.heading("film_id", text="Код")
        self.films_tree.heading("director", text="Режиссёр")
        self.films_tree.heading("title", text="Фильм")
        self.films_tree.heading("holder", text="Статус / Владелец")

        self.films_tree.column("film_id", width=75, anchor=tk.CENTER)
        self.films_tree.column("director", width=210)
        self.films_tree.column("title", width=270)
        self.films_tree.column("holder", width=160)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.films_tree.yview)
        self.films_tree.configure(yscroll=scrollbar.set)

        self.films_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        test_data = [
            ("001", "Квентин Тарантино", "Криминальное чтиво", "Иванов И.И."),
            ("002", "Кристофер Нолан", "Интерстеллар", "В фильмотеке"),
            ("003", "Квентин Тарантино", "Бешеные псы", "Петров П.П."),
        ]
        for row in test_data:
            self.films_tree.insert("", tk.END, values=row)

        search_frame = ttk.Frame(self.root, padding=6)
        search_frame.pack(side=tk.BOTTOM, fill=tk.X)

        ttk.Label(search_frame, text="Режиссёр:").pack(side=tk.LEFT, padx=3)
        self.director_combo = ttk.Combobox(search_frame, values=[])
        self.director_combo.set("Все режиссёры")
        self.director_combo.pack(side=tk.LEFT, padx=3)

        ttk.Label(search_frame, text="Название фильма:").pack(side=tk.LEFT, padx=3)
        self.search_entry = ttk.Entry(search_frame, width=24)
        self.search_entry.pack(side=tk.LEFT, padx=3)

        btn_search = ttk.Button(search_frame, text="Поиск", command=lambda: None)
        btn_search.pack(side=tk.LEFT, padx=6)

if __name__ == "__main__":
    root = tk.Tk()
    app = FilmLibraryApp(root)
    app.create_interface()
    root.mainloop()
