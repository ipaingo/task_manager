import unittest
from main import find_user, users
from user import User

class TestMain(unittest.TestCase):

    def setUp(self):
        """Подготовка данных перед каждым тестом."""
        users.clear()  # Очищаем список пользователей перед каждым тестом
        self.user1 = User("Alice")
        self.user2 = User("Bob")
        users.append(self.user1)
        users.append(self.user2)

    def test_find_user_existing(self):
        """Тест поиска существующего пользователя."""
        user = find_user("Alice")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "Alice")

    def test_find_user_non_existing(self):
        """Тест поиска несуществующего пользователя."""
        user = find_user("Charlie")
        self.assertIsNone(user)

    def test_find_user_case_sensitive(self):
        """Тест поиска с учётом регистра."""
        user = find_user("alice")
        self.assertIsNone(user)

    def test_add_user(self):
        """Тест добавления нового пользователя."""
        new_user = User("Charlie")
        users.append(new_user)
        self.assertIn(new_user, users)
        self.assertEqual(len(users), 3)

    def test_remove_user(self):
        """Тест удаления пользователя."""
        users.remove(self.user1)
        self.assertNotIn(self.user1, users)
        self.assertEqual(len(users), 1)


if __name__ == "__main__":
    unittest.main()
