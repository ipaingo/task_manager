
import unittest
from task import Task

class TestTask(unittest.TestCase):

    def setUp(self):
        """Подготовка данных перед каждым тестом."""
        self.task = Task("Задача 1", "Описание 1", time="10:00-12:00", location="Офис")

    def test_get_info(self):
        """Тест получения информации о задаче."""
        info = self.task.get_info()
        self.assertIn("Задача 1", info)
        self.assertIn("Описание 1", info)
        self.assertIn("10:00-12:00", info)

    def test_update_status(self):
        """Тест обновления статуса задачи."""
        self.task.update_status("In Progress")
        self.assertEqual(self.task.status, "In Progress")

    def test_update_description(self):
        """Тест обновления описания задачи."""
        self.task.update_description("Описание 2")
        self.assertEqual(self.task.description, "Описание 2")

    def test_update_location(self):
        """Тест обновления местоположения задачи"""
        self.task.update_location("Дом")
        self.assertEqual(self.task.location, "Дом")

    def test_update_time_valid(self):
        """Тест обновления времени на корректное значение."""
        self.assertTrue(self.task.update_time("Не указано"))
        self.assertEqual(self.task.time, "Не указано")
        self.assertTrue(self.task.update_time("10:00-11:00"))
        self.assertEqual(self.task.time, "10:00-11:00")

    def test_update_time_invalid(self):
        """Тест обновления времени на некорректное значение."""
        self.assertFalse(self.task.update_time("11:00-10:00"))
        self.assertFalse(self.task.update_time("10:00;11:00"))
        self.assertFalse(self.task.update_time("10:00-11;00"))
        self.assertFalse(self.task.update_time("123:00-11:00"))
        self.assertFalse(self.task.update_time("10:00-11:456"))
        self.assertFalse(self.task.update_time("аа:бб-вв:гг"))
        self.assertFalse(self.task.update_time("10:60-25:00"))
        self.assertFalse(self.task.update_time("10:00-25:00"))

    def test_update_all(self):
        """Тест обновления всех параметров задачи."""
        self.task.update_all("Completed", "New Description", "15:00-16:00", "Home")
        self.assertEqual(self.task.status, "Completed")
        self.assertEqual(self.task.description, "New Description")
        self.assertEqual(self.task.time, "15:00-16:00")
        self.assertEqual(self.task.location, "Home")


if __name__ == "__main__":
    unittest.main()
