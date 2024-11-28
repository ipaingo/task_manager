import unittest
from usermanager import *

class TestUserManager(unittest.TestCase):
    def setUp(self):
        """Подготовка данных перед каждым тестом."""
        users.clear()  # Очищаем список пользователей перед каждым тестом
        self.user1 = User("Анна")
        self.user2 = User("Иван")
        users.append(self.user1)
        users.append(self.user2)

    def test_find_user_existing(self):
        """Тест поиска существующего пользователя."""
        user = find_user("Анна")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "Анна")

    def test_find_user_non_existing(self):
        """Тест поиска несуществующего пользователя."""
        user = find_user("Сергей")
        self.assertIsNone(user)

    def test_find_user_case_sensitive(self):
        """Тест поиска с учётом регистра."""
        user = find_user("анна")
        self.assertIsNone(user)

    def test_add_user(self):
        """Тест добавления нового пользователя."""
        add_user("Сергей")
        self.assertEqual(len(users), 3)

    def test_add_duplicate_user(self):
        add_user("Анна")
        self.assertEqual(len(users), 2)

    def test_remove_user(self):
        """Тест удаления пользователя."""
        remove_user("Иван")
        self.assertNotIn("Иван", users)
        self.assertEqual(len(users), 1)

    def test_remove_user_unknown(self):
        remove_user("Сергей")
        self.assertEqual(len(users), 2)

    def test_get_userlist(self):
        self.assertTrue(get_userlist())

    def test_get_empty_userlist(self):
        users.clear()
        self.assertFalse(get_userlist())
