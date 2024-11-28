import unittest
from user import User
from task import Task

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Метод setUp создаёт объект пользователя и несколько задач для тестирования.
        """
        self.user = User("Иван")
        self.task1 = Task("Задача 1", "Описание 1", status="To Do", time="09:00-10:00", location="Офис")
        self.task2 = Task("Задача 2", "Описание 2", status="In Progress", time="10:00-11:00", location="Дом")
        self.duplicate_task = Task("Задача 1", "Дубликат задачи", status="To Do", time="11:00-12:00", location="Удалёнка")

    def test_add_task_success(self):
        """Тест успешного добавления задачи."""
        self.user.add_task(self.task1)
        self.assertEqual(len(self.user.tasks), 1)
        self.assertEqual(self.user.tasks[0].title, "Задача 1")

    def test_add_duplicate_task(self):
        """Тест добавления задачи с дублирующимся названием."""
        self.user.add_task(self.task1)
        self.user.add_task(self.duplicate_task)
        self.assertEqual(len(self.user.tasks), 1)

    def test_remove_task_success(self):
        """Тест успешного удаления задачи."""
        self.user.add_task(self.task1)
        self.assertTrue(self.user.remove_task("Задача 1"))
        self.assertEqual(len(self.user.tasks), 0)

    def test_remove_task_not_found(self):
        """Тест попытки удаления несуществующей задачи."""
        self.assertFalse(self.user.remove_task("Несуществующая задача"))

    def test_get_info(self):
        """Тест метода get_info()."""
        self.user.add_task(self.task1)
        self.user.add_task(self.task2)
        expected_info = (
            "Пользователь: Иван\n"
            "     Задачи:\n"
            "Задача: Задача 1\n"
            "Описание: Описание 1\n"
            "Статус: To Do\n"
            "Время: 09:00-10:00\n"
            "Место: Офис\n"
            "Задача: Задача 2\n"
            "Описание: Описание 2\n"
            "Статус: In Progress\n"
            "Время: 10:00-11:00\n"
            "Место: Дом\n"
        )
        self.assertEqual(self.user.get_info(), expected_info)

    def test_find_task_by_title(self):
        """Тест поиска задачи по названию."""
        self.user.add_task(self.task1)
        found_task = self.user._find_task_by_title("Задача 1")
        self.assertIsNotNone(found_task)
        self.assertEqual(found_task.title, "Задача 1")

    def test_find_task_by_title_not_found(self):
        """Тест поиска задачи, которой нет в списке."""
        self.user.add_task(self.task1)
        found_task = self.user._find_task_by_title("Несуществующая задача")
        self.assertIsNone(found_task)

    def test_is_task_duplicate(self):
        """Тест проверки дублирования задач."""
        self.user.add_task(self.task1)
        self.assertTrue(self.user._is_task_duplicate(self.duplicate_task))
        self.assertFalse(self.user._is_task_duplicate(self.task2))


if __name__ == "__main__":
    unittest.main()
