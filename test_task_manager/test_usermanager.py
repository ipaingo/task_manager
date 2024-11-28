import unittest
from user import User
from task import Task

class TestUserManager(unittest.TestCase):
    def setUp(self):
        """Подготовка данных перед каждым тестом."""
        self.user = User("Анна")
        self.task1 = Task("Задача 1", "Описание 1")
        self.task2 = Task("Задача 2", "Описание 2")

    def test_add_task(self):
        """Тест добавления задачи пользователю."""
        self.user.add_task(self.task1)
        self.assertIn(self.task1, self.user.tasks)

    def test_add_duplicate_task(self):
        """Тест добавления дубликата задачи."""
        self.user.add_task(self.task1)
        self.user.add_task(self.task1)  # Попытка добавить ту же задачу
        self.assertEqual(len(self.user.tasks), 1)

    def test_get_info(self):
        """Тест получения информации о пользователе и его задачах."""
        self.user.add_task(self.task1)
        info = self.user.get_info()
        self.assertIn("Анна", info)
        self.assertIn("Задача 1", info)

    def test_remove_task(self):
        """Тест удаления задачи по названию."""
        self.user.add_task(self.task1)
        self.user.remove_task("Задача 1")
        self.assertNotIn(self.task1, self.user.tasks)

    def test_remove_non_existing_task(self):
        """Тест удаления несуществующей задачи."""
        result = self.user.remove_task("NonExistingTask")
        self.assertFalse(result)