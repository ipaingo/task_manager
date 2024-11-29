class Task:
    NOT_SPECIFIED = "Не указано"

    def __init__(self, title, description, status="To Do", time=NOT_SPECIFIED, location=NOT_SPECIFIED):
        """
        Инициализация задачи.
        :param title: Название задачи.
        :param description: Описание задачи.
        :param status: Статус задачи (по умолчанию "To Do").
        :param time: Время выполнения задачи (формат HH:MM-HH:MM).
        :param location: Местоположение выполнения задачи.
        """
        self.title = title
        self.description = description
        self.status = status
        self.time = time
        self.location = location

    def get_info(self):
        return (f"Задача: {self.title}\n"
                f"Описание: {self.description}\n"
                f"Статус: {self.status}\n"
                f"Время: {self.time}\n"
                f"Место: {self.location}\n")

    def update_status(self, status):
        """
        Обновить статус задачи.
        :param status: Новый статус.
        """

        self.status = status

    def update_description(self, description):
        """
        Обновить описание задачи.
        :param description: Новое описание.
        """
        self.description = description

    def update_time(self, time):
        """
        Обновить время выполнения задачи.
        :param time: Новое время выполнения задачи (формат HH:MM-HH:MM).
        """
        self.time = time

    def update_location(self, location):
        """
        Обновить местоположение выполнения задачи.
        :param location: Новое местоположение.
        """
        self.location = location

    def update_all(self, status, description, time, location):
        """
        Обновить все параметры задачи.
        :param status: Новый статус.
        :param description: Новое описание.
        :param time: Новое время выполнения.
        :param location: Новое местоположение.
        """
        self.status = status
        self.description = description
        self.time = time
        self.location = location

    def is_valid_time(self, time):
        """
        Проверяет корректность формата времени HH:MM-HH:MM.
        :param time: Строка времени.
        :return: True, если формат времени корректен, иначе False.
        """
        if time == Task.NOT_SPECIFIED:
            return True

        # Проверить разделитель '-'
        if time.count('-') != 1:
            return False

        # Разделить строку на время начала и окончания
        start_time, end_time = time.split('-')

        # Проверить разделитель ':'
        if start_time.count(':') != 1 or end_time.count(':') != 1:
            return False

        # Извлечь часы и минуты
        start_hours, start_minutes = start_time.split(':')[0], start_time.split(':')[1]
        end_hours, end_minutes = end_time.split(':')[0], end_time.split(':')[1]

        # Проверить длину элементов
        if len(start_hours) < 1 or len(start_hours) > 2 or len(end_hours) < 1 or len(end_hours) > 2:
            return False
        if len(start_minutes) != 2 or len(end_minutes) != 2:
            return False

        # Проверить, что время является числовым значением
        if not(start_hours.isdigit() and start_minutes.isdigit() and end_hours.isdigit() and end_minutes.isdigit()):
            return False

        start_hours = int(start_hours)
        start_minutes = int(start_minutes)
        end_hours = int(end_hours)
        end_minutes = int(end_minutes)

        # Проверить диапазоны значений
        if not (0 <= start_hours <= 23 and 0 <= start_minutes <= 59):
            return False
        if not (0 <= end_hours <= 23 and 0 <= end_minutes <= 59):
            return False

        # Убедиться, что время начала меньше времени окончания
        if start_hours > end_hours or (start_hours == end_hours and start_minutes > end_minutes):
            return False

        return True
