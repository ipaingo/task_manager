import unittest
from main import *

class TestAcceptance(unittest.TestCase):
    def setUp(self):
        """Очищаем глобальный список пользователей перед каждым тестом."""
        global users
        users.clear()

    def test_full_scenario(self):
        """Полный сценарий работы Task Manager."""
        # 1. Добавить двух пользователей
        add_user("Иван")
        add_user("Мария")
        self.assertEqual(len(users), 2)

        # 2. Добавить задачи пользователям
        user_ivan = find_user("Иван")
        user_maria = find_user("Мария")

        task1 = Task("Задача 1", "Описание 1", time="09:00-10:00", location="Офис")
        task2 = Task("Задача 2", "Описание 2", time="10:00-11:00", location="Дом")

        user_ivan.add_task(task1)
        user_maria.add_task(task2)

        self.assertEqual(len(user_ivan.tasks), 1)
        self.assertEqual(len(user_maria.tasks), 1)

        # 3. Обновить статус задачи у Ивана
        user_ivan.tasks[0].update_status("Completed")
        self.assertEqual(user_ivan.tasks[0].status, "Completed")

        # 4. Удалить задачу у Марии
        removed = user_maria.remove_task("Задача 2")
        self.assertTrue(removed)
        self.assertEqual(len(user_maria.tasks), 0)

        # 5. Удалить пользователя Ивана
        remove_user("Иван")
        self.assertIsNone(find_user("Иван"))

        # 6. Проверить, что Мария осталась в списке
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].name, "Мария")


if __name__ == "__main__":
    unittest.main()
