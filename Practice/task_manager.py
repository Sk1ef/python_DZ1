import json


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description: str):
        task = {
            "description": description,
            "completed": False
        }

        if task in self.tasks:
            print("Задача уже есть")
        else:
            self.tasks.append(task)
            print("Задача добавлена")

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Задачи нет")

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Задачи нет")

    def save_to_json(self, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file)
            print("Файл сохранен")

    def load_from_json(self, filename: str):
        with open(filename, "r", encoding="utf-8") as file:
            self.tasks = json.load(file)
            print("Задачи загружены")

    def main(self):
        menu = {
            1: ("Добавить новую задачу", self.add_task),
            2: ("Выполнить задачу", self.complete_task),
            3: ("Удалить задачу", self.remove_task),
            4: ("Сохранить в json", self.save_to_json),
            5: ("Загрузить из json", self.load_from_json),
            6: ("Выход", None)
        }

        while True:
            for number in menu:
                print(f"{number}. {menu[number][0]}")

            try:
                num = int(input("Введите номер операции от 1 до 6: "))
            except ValueError:
                print("Введено не число")
                continue

            if num not in menu:
                print("Неверный номер операции")
                continue

            if num == 6:
                print("Работа завершена")
                break

            if num == 1:
                value = input("Введите задачу: ")
                menu[num][1](value)

            elif num == 2 or num == 3:
                try:
                    value = int(input("Введите индекс задачи: "))
                except ValueError:
                    print("Введено не число")
                    continue

                menu[num][1](value)

            elif num == 4 or num == 5:
                value = input("Введите имя файла: ")
                menu[num][1](value)


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.main()