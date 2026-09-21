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


todo = ToDoList()

todo.add_task("Купить продукты")
todo.add_task("Прочитать главу книги")
todo.add_task("Сделать зарядку")

todo.list_tasks()

todo.complete_task("Купить продукты")
todo.complete_task("Полить цветы")

todo.list_tasks()

todo.remove_task("Сделать зарядку")
todo.remove_task("Полить цветы")

todo.list_tasks()
