import unittest
from task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        """
        Метод setUp запускается перед каждым тестом.
        Создаем базовую задачу для тестирования.
        """
        self.task = Task(
            title="Тестовая задача",
            description="Тестовое описание",
            status="К выполнению",
            time="09:00-10:00",
            location="Офис"
        )

    def test_initialization(self):
        """Тест на корректную инициализацию задачи."""
        self.assertEqual(self.task.title, "Тестовая задача")
        self.assertEqual(self.task.description, "Тестовое описание")
        self.assertEqual(self.task.status, "К выполнению")
        self.assertEqual(self.task.time, "09:00-10:00")
        self.assertEqual(self.task.location, "Офис")

    def test_get_info(self):
        """Тест корректности метода get_info()."""
        expected_info = (
            "Задача: Тестовая задача\n"
            "Описание: Тестовое описание\n"
            "Статус: К выполнению\n"
            "Время: 09:00-10:00\n"
            "Место: Офис\n"
        )
        self.assertEqual(self.task.get_info(), expected_info)

    def test_update_status(self):
        """Проверяем обновление статуса задачи."""
        self.task.update_status("В процессе")
        self.assertEqual(self.task.status, "В процессе")

    def test_update_description(self):
        """Проверяем обновление описания задачи."""
        self.task.update_description("Обновленное описание")
        self.assertEqual(self.task.description, "Обновленное описание")

    def test_update_time(self):
        """Проверяем обновление времени выполнения задачи."""
        self.task.update_time("10:00-11:00")
        self.assertEqual(self.task.time, "10:00-11:00")

    def test_update_location(self):
        """Проверяем обновление местоположения."""
        self.task.update_location("Дом")
        self.assertEqual(self.task.location, "Дом")

    def test_update_all(self):
        """Проверяем массовое обновление параметров."""
        self.task.update_all(
            status="Завершено",
            description="Полностью обновлено",
            time="11:00-12:00",
            location="Удаленно"
        )
        self.assertEqual(self.task.status, "Завершено")
        self.assertEqual(self.task.description, "Полностью обновлено")
        self.assertEqual(self.task.time, "11:00-12:00")
        self.assertEqual(self.task.location, "Удаленно")

    def test_valid_time_correct(self):
        """Тестируем корректные значения времени."""
        self.assertTrue(self.task.is_valid_time("09:00-10:00"))
        self.assertTrue(self.task.is_valid_time("00:00-23:59"))
        self.assertTrue(self.task.is_valid_time("Не указано"))

    def test_valid_time_incorrect(self):
        """Тестируем некорректные значения времени."""
        self.assertFalse(self.task.is_valid_time("25:00-26:00"))
        self.assertFalse(self.task.is_valid_time("12:60-13:00"))
        self.assertFalse(self.task.is_valid_time("10:00-09:00"))
        self.assertFalse(self.task.is_valid_time("09:00-"))
        self.assertFalse(self.task.is_valid_time("09-10:00"))
        self.assertFalse(self.task.is_valid_time("09:00;10:00"))

    def test_valid_time_edge_cases(self):
        """Тестируем пограничные случаи времени."""
        self.assertFalse(self.task.is_valid_time(""))
        self.assertFalse(self.task.is_valid_time("09:00-09:"))
        self.assertTrue(self.task.is_valid_time("00:00-00:01"))
        self.assertTrue(self.task.is_valid_time("23:58-23:59"))


if __name__ == "__main__":
    unittest.main()
