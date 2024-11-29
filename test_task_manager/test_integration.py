import unittest
from usermanager import users, find_user, add_user, remove_user, get_userlist
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
        add_user("Диана")
        user = find_user("Диана")
        task = Task("Новая задача", "Описание")
        user.add_task(task)
        task.update_status("Выполняется")
        task.update_description("Обновлённое описание")
        self.assertEqual(task.status, "Выполняется")
        self.assertEqual(task.description, "Обновлённое описание")
