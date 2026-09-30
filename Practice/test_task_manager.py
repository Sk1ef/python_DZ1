from task_manager import TaskManager


def test_add_and_complete_task():
    manager = TaskManager()

    manager.add_task("Сделать домашку")
    manager.complete_task(0)

    assert manager.tasks[0]["description"] == "Сделать домашку"
    assert manager.tasks[0]["completed"] is True


def test_remove_task():
    manager = TaskManager()

    manager.add_task("Удалить эту задачу")
    manager.remove_task(0)

    assert len(manager.tasks) == 0


def test_save_and_load_json():
    manager = TaskManager()

    manager.add_task("Сохранить задачу")
    manager.complete_task(0)

    filename = r"C:\Users\User\PycharmProjects\Vladimir_Izosimov\Practice\test_tasks.json"

    manager.save_to_json(filename)

    new_manager = TaskManager()
    new_manager.load_from_json(filename)

    assert new_manager.tasks == manager.tasks
