import tkinter as tk
from tkinter import ttk, messagebox


class FilmLibraryApp:
    """
    Класс «Приложение».
    Реализует графический интерфейс для учёта фильмов в фильмотеке.
    """

    def __init__(self, root):
        """Инициализация главного окна приложения."""
        self.root = root
        self.root.title("Фильмотека")
        self.root.geometry("800x500")

    def create_interface(self):
        """
        Метод построения и визуализации экранной формы.
        Создаёт панель инструментов, таблицу фильмов и панель поиска.
        """
        toolbar = ttk.Frame(self.root, padding=6)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_save = ttk.Button(toolbar, text="Сохранить", command=self.on_save)
        btn_save.pack(side=tk.LEFT, padx=3)

        btn_add = ttk.Button(toolbar, text="Добавить", command=self.on_add)
        btn_add.pack(side=tk.LEFT, padx=3)

        btn_delete = ttk.Button(toolbar, text="Удалить", command=self.on_delete)
        btn_delete.pack(side=tk.LEFT, padx=3)

        btn_edit = ttk.Button(toolbar, text="Редактировать", command=self.on_edit)
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

        scrollbar = ttk.Scrollbar(
            table_frame, orient=tk.VERTICAL, command=self.films_tree.yview
        )
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

        self.films_tree.bind("<Double-1>", self.on_table_click)

        search_frame = ttk.Frame(self.root, padding=6)
        search_frame.pack(side=tk.BOTTOM, fill=tk.X)

        ttk.Label(search_frame, text="Режиссёр:").pack(side=tk.LEFT, padx=3)
        self.director_combo = ttk.Combobox(
            search_frame,
            values=["Все режиссёры", "Квентин Тарантино", "Кристофер Нолан"],
        )
        self.director_combo.set("Все режиссёры")
        self.director_combo.pack(side=tk.LEFT, padx=3)

        self.director_combo.bind("<<ComboboxSelected>>", self.on_director_select)

        ttk.Label(search_frame, text="Название фильма:").pack(side=tk.LEFT, padx=3)
        self.search_entry = ttk.Entry(search_frame, width=24)
        self.search_entry.pack(side=tk.LEFT, padx=3)

        btn_search = ttk.Button(search_frame, text="Поиск", command=self.on_search)
        btn_search.pack(side=tk.LEFT, padx=6)

    def on_save(self):
        """Обработчик нажатия кнопки 'Сохранить'."""
        messagebox.showinfo("Сохранение", "Каталог фильмов сохранён (имитация).")

    def on_add(self):
        """Обработчик нажатия кнопки 'Добавить'."""
        self.films_tree.insert(
            "", tk.END, values=("004", "Новый Режиссёр", "Новый Фильм", "В фильмотеке")
        )
        messagebox.showinfo("Добавление", "Добавлен новый фильм.")

    def on_delete(self):
        """Обработчик нажатия кнопки 'Удалить'."""
        selected_items = self.films_tree.selection()
        if not selected_items:
            messagebox.showwarning("Удаление", "Выберите строку для удаления!")
            return
        for item in selected_items:
            self.films_tree.delete(item)
        messagebox.showinfo("Удаление", "Запись о фильме удалена.")

    def on_edit(self):
        """Обработчик нажатия кнопки 'Редактировать'."""
        selected_items = self.films_tree.selection()
        if not selected_items:
            messagebox.showwarning(
                "Редактирование", "Выберите строку для редактирования!"
            )
            return
        messagebox.showinfo(
            "Редактирование", "Редактирование выбранного фильма (имитация)."
        )

    def on_search(self):
        """
        Обработчик нажатия кнопки 'Поиск'.
        Проверяет корректность ввода и ищет фильм по названию в таблице.
        """
        search_text = self.search_entry.get().strip()
        if not search_text or search_text == "Название фильма":
            messagebox.showinfo(
                "Ошибка поиска", "Вы не ввели название фильма для поиска"
            )
            return

        found = False
        for child in self.films_tree.get_children():
            values = self.films_tree.item(child, "values")
            if search_text.lower() in values[2].lower():
                self.films_tree.selection_set(child)
                found = True
                break

        if found:
            messagebox.showinfo("Поиск", f"Фильм по запросу '{search_text}' найден.")
        else:
            messagebox.showinfo(
                "Поиск", f"Фильм по запросу '{search_text}' не найден."
            )

    def on_director_select(self, event):
        """
        Слушатель выбора элемента в выпадающем списке режиссёров.
        Выводит сообщение с выбранным режиссёром.
        """
        selected = self.director_combo.get()
        messagebox.showinfo("Выбор списка", f"Выбран режиссёр: {selected}")

    def on_table_click(self, event):
        """
        Слушатель двойного щелчка мыши по строке таблицы.
        Выводит информацию о выбранном названии фильма.
        """
        selected_item = self.films_tree.selection()
        if selected_item:
            values = self.films_tree.item(selected_item[0], "values")
            messagebox.showinfo("Таблица", f"Выбран фильм: {values[2]}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FilmLibraryApp(root)
    app.create_interface()
    root.mainloop()