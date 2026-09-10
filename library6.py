def book_list_view(library):
    if not library:
        print("Книг нет")
    else:
        for key in library:
            print(key)


def add_book(library, title, author, year):
    if title in library:
        answer = input("Такая книга уже существует. Обновить информацию? (да/нет): ")
        if answer.lower() == "да":
            print(f'Информация о книге "{title}" успешно обновлена.')
        else:
            print("Информация не была изменена.")
            return
    else:
        print(f'Книга "{title}" успешно добавлена.')

    library[title] = {
        "автор": author,
        "год": year,
        "наличие": library[title]["наличие"] if title in library else None
    }


def remove_book(library, title):
    if title in library:
        del library[title]
        print(f'Книга "{title}" успешно удалена')
    else:
        print("Книга не найдена")


def issue_book(library, title):
    if title in library:
        library[title]["наличие"] = False
        print(f'Книга "{title}" выдана')
    else:
        print("Книги нет")


def return_book(library, title):
    if title in library:
        library[title]["наличие"] = True
        print(f'Книга "{title}" в наличии')
    else:
        print("Книги нет")


def find_book(library, title):
    if title in library:
        print(f'Информация о книге "{title}": \n{library[title]}')
        if library[title]["наличие"] is None:
            print("Книга в библиотеке, но ее статус не определен")
        elif library[title]["наличие"] is False:
            print("Книга выдана")
        else:
            print("Книга доступна")
    else:
        print("Книги нет")


library = {
    "Гарри Поттер и философский камень": {
        "автор": "Дж. К. Роулинг",
        "год": 1997,
        "наличие": True
    },
    "Война и мир": {
        "автор": "Лев Толстой",
        "год": 1869,
        "наличие": False
    },
    "1984": {
        "автор": "Джордж Оруэлл",
        "год": 1949,
        "наличие": True
    },
    "Мастер и Маргарита": {
        "автор": "Михаил Булгаков",
        "год": 1967,
        "наличие": False
    }
}

remove_book(library, "Мастер и Маргарита")
add_book(library, "Преступление и наказание", "Фёдор Достоевский", 1866)
issue_book(library, "Гарри Поттер и философский камень")
return_book(library, "Война и мир")
find_book(library, "1984")
book_list_view(library)
