import unittest
from usermanager import *
from task import Task

class TestIntegration(unittest.TestCase):
    def setUp(self):
        """Подготовка тестовой среды. Очищаем список пользователей перед каждым тестом."""
        users.clear()

    def test_add_user_and_task(self):
        """Проверка добавления пользователя и задачи."""
        add_user("Алиса")
        user = find_user("Алиса")
        self.assertIsNotNone(user)
        task = Task("Задачка", "Описание для задачки")
        user.add_task(task)
        self.assertEqual(len(user.tasks), 1)
        self.assertEqual(user.tasks[0].title, "Задачка")

    def test_remove_user_with_tasks(self):
        """Проверка удаления пользователя вместе с его задачами."""
        add_user("Чарли")
        user = find_user("Чарли")
        task = Task("Задача", "Очередная, ничего нового")
        user.add_task(task)
        remove_user("Чарли")
        self.assertIsNone(find_user("Чарли"))
        self.assertEqual(len(users), 0)

    def test_get_userlist(self):
        """Проверка получения списка пользователей и их задач."""
        add_user("Ева")
        user = find_user("Ева")
        task = Task("Важная Задача", "Сделать как можно быстрее")
        user.add_task(task)
        result = get_userlist()
        self.assertTrue(result)

    def test_update_task_info(self):
        """Проверка обновления информации о задаче."""
        add_user("Diana")
        user = find_user("Diana")
        task = Task("Task2", "Initial description")
        user.add_task(task)
        task.update_status("In Progress")
        task.update_description("Updated description")
        self.assertEqual(task.status, "In Progress", "Статус задачи должен обновиться.")
        self.assertEqual(task.description, "Updated description", "Описание задачи должно обновиться.")
