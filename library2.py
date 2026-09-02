def book_list_view(library):
    if not library:
        print("Книг нет")
    else:
        for key in library:
            print(key)


def add_book(title, author, year):
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


library = {
    "Гарри Поттер и философский камень": {
        "автор": "Дж. К. Роулинг",
        "год": 1997,
        "наличие": "в наличии"
    },
    "Война и мир": {
        "автор": "Лев Толстой",
        "год": 1869,
        "наличие": "выдана"
    },
    "1984": {
        "автор": "Джордж Оруэлл",
        "год": 1949,
        "наличие": "в наличии"
    },
    "Мастер и Маргарита": {
        "автор": "Михаил Булгаков",
        "год": 1967,
        "наличие": "в наличии"
    }
}

add_book("Преступление и наказание", "Фёдор Достоевский", 1866)
book_list_view(library)
