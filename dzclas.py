class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task in self.tasks:
            print(f"Задача '{task}' уже есть в списке.")
        else:
            self.tasks[task] = False
            print(f"Задача '{task}' успешно добавлена.")

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks[task] = True
            print(f"Задача '{task}' отмечена как выполненная.")
        else:
            print(f"Задача '{task}' не найдена.")

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
            print(f"Задача '{task}' удалена.")
        else:
            print(f"Задача '{task}' не найдена.")

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("Список задач:")
        for task, completed in self.tasks.items():
            status = "✓" if completed else " "
            print(f"[{status}] {task}")

    def main(self):
        menu = {
            1: ("Добавить новую задачу", self.add_task),
            2: ("Выполнить задачу", self.complete_task),
            3: ("Удалить задачу", self.remove_task),
            4: ("Показать задачи", self.list_tasks),
            5: ("Выход", None)
        }

        while True:
            for number in menu:
                print(f"{number}. {menu[number][0]}")

            try:
                num = int(input("Введите номер операции от 1 до 5: "))
            except ValueError:
                print("Введено не число")
                continue

            if num not in menu:
                print("Неверный номер операции")
                continue

            if num == 5:
                print("Работа завершена")
                break

            if num == 4:
                menu[num][1]()
            else:
                task = input("Введите задачу: ")
                menu[num][1](task)


todo = ToDoList()
todo.main()
