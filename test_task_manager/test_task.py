import unittest
from task import Task

class TestTask(unittest.TestCase):

    def setUp(self):
        """Подготовка данных перед каждым тестом."""
        self.task = Task("Task1", "Description1", time="10:00-12:00", location="Office")

    def test_get_info(self):
        """Тест получения информации о задаче."""
        info = self.task.get_info()
        self.assertIn("Task1", info)
        self.assertIn("Description1", info)
        self.assertIn("10:00-12:00", info)

    def test_update_status(self):
        """Тест обновления статуса задачи."""
        self.task.update_status("In Progress")
        self.assertEqual(self.task.status, "In Progress")

    def test_update_time_valid(self):
        """Тест обновления времени на корректное значение."""
        self.task.update_time("13:00-14:00")
        self.assertEqual(self.task.time, "13:00-14:00")

    def test_update_time_invalid(self):
        """Тест обновления времени на некорректное значение."""
        self.assertFalse(self.task.is_valid_time("14:00-13:00"))

    def test_update_all(self):
        """Тест обновления всех параметров задачи."""
        self.task.update_all("Completed", "New Description", "15:00-16:00", "Home")
        self.assertEqual(self.task.status, "Completed")
        self.assertEqual(self.task.description, "New Description")
        self.assertEqual(self.task.time, "15:00-16:00")
        self.assertEqual(self.task.location, "Home")


if __name__ == "__main__":
    unittest.main()
