# Модуль test_usermanager.py

### Тест Блочный 1: Положительный (Тест поиска существующего пользователя)
**Цель:** Проверить поиск существующего пользователя.  
**Входные данные:** Список пользователей содержит User("Анна"), вызов `find_user("Анна")`.  
**Ожидаемый результат:** Найден пользователь с именем "Анна".  
**Описание процесса:** Добавляем двух пользователей в список (`Анна`, `Иван`), вызываем функцию поиска, проверяем, что возвращается объект нужного пользователя с именем "Анна".  

---

### Тест Блочный 2: Отрицательный (Тест поиска несуществующего пользователя)
**Цель:** Проверить корректность поведения при поиске несуществующего пользователя.  
**Входные данные:** Список пользователей содержит User("Анна"), User("Иван"), вызов `find_user("Сергей")`.  
**Ожидаемый результат:** Возвращается `None`.  
**Описание процесса:** Список содержит двух пользователей, выполняется поиск пользователя "Сергей". Убедиться, что результатом выполнения функции является `None`.  

---

### Тест Блочный 3: Отрицательный (Тест поиска с учётом регистра)
**Цель:** Убедиться, что поиск пользователя чувствителен к регистру.  
**Входные данные:** Список пользователей содержит User("Анна"), вызов `find_user("анна")`.  
**Ожидаемый результат:** Возвращается `None`.  
**Описание процесса:** Добавляем пользователей в список, вызываем поиск по имени в другом регистре и проверяем, что результат равен `None`.  

---

### Тест Блочный 4: Положительный (Тест добавления нового пользователя)
**Цель:** Проверить корректность добавления нового пользователя в список.  
**Входные данные:** Список пользователей содержит User("Анна"), User("Иван"), вызов `add_user("Сергей")`.  
**Ожидаемый результат:** Длина списка пользователей увеличивается на 1, итоговый список содержит трёх пользователей.  
**Описание процесса:** Добавляем нового пользователя "Сергей", проверяем размер списка пользователей и наличие нового пользователя в списке.  

---

### Тест Блочный 5: Негативный (Тест добавления пустого имени пользователя)  
**Цель:** Проверить обработку попытки добавить пользователя с пустым именем.  
**Входные данные:** Список пользователей изначально содержит двух пользователей. Вызов `add_user("    ")`.  
**Ожидаемый результат:** Пользователь с пустым именем не добавляется, длина списка пользователей остаётся равной 2.  
**Описание процесса:** Вызываем функцию добавления пользователя с пустым именем, проверяем, что список пользователей не изменился, и пользователь с пустым именем не был добавлен.

---

### Тест Блочный 6: Отрицательный (Тест добавления дублирующего пользователя)
**Цель:** Убедиться, что попытка добавить уже существующего пользователя не изменяет список.  
**Входные данные:** Список пользователей содержит User("Анна"), вызов `add_user("Анна")`.  
**Ожидаемый результат:** Длина списка пользователей остаётся неизменной.  
**Описание процесса:** Пытаемся добавить пользователя с именем "Анна", который уже есть в списке, проверяем, что длина списка остаётся 2.  

---

### Тест Блочный 7: Положительный (Тест удаления существующего пользователя)
**Цель:** Проверить корректность удаления существующего пользователя.  
**Входные данные:** Список пользователей содержит User("Анна"), User("Иван"), вызов `remove_user("Иван")`.  
**Ожидаемый результат:** Длина списка пользователей уменьшается на 1, пользователь "Иван" отсутствует в списке.  
**Описание процесса:** Удаляем пользователя "Иван", проверяем размер списка и отсутствие этого пользователя в списке.  

---

### Тест Блочный 8: Отрицательный (Тест удаления несуществующего пользователя)
**Цель:** Проверить, что удаление несуществующего пользователя не изменяет список.  
**Входные данные:** Список пользователей содержит User("Анна"), User("Иван"), вызов `remove_user("Сергей")`.  
**Ожидаемый результат:** Длина списка остаётся неизменной.  
**Описание процесса:** Пытаемся удалить пользователя с именем "Сергей", которого нет в списке, проверяем, что длина списка остаётся равной 2.  

---

### Тест Блочный 9: Положительный (Тест получения списка пользователей)
**Цель:** Проверить, что функция возвращает список пользователей, если он не пуст.  
**Входные данные:** Список пользователей содержит User("Анна"), User("Иван"), вызов `get_userlist()`.  
**Ожидаемый результат:** Функция возвращает `True`, список пользователей не пуст.  
**Описание процесса:** Вызываем функцию получения списка, проверяем, что она возвращает непустой список.  

---

### Тест Блочный 10: Отрицательный (Тест получения пустого списка пользователей)
**Цель:** Убедиться, что функция возвращает пустой список, если в системе нет пользователей.  
**Входные данные:** Список пользователей пуст, вызов `get_userlist()`.  
**Ожидаемый результат:** Функция возвращает `False`, список пользователей пуст.  
**Описание процесса:** Очищаем список пользователей, вызываем функцию получения списка, проверяем, что результат соответствует ожиданиям.  

# Модуль test_user.py

### Тест Блочный 1: Положительный (Тест добавления задачи пользователю)
**Цель:** Проверить корректность добавления задачи пользователю.  
**Входные данные:** Пользователь `Анна`, задача `Задача 1`. Вызов `self.user.add_task(self.task1)`.  
**Ожидаемый результат:** Задача `Задача 1` добавлена в список задач пользователя.  
**Описание процесса:** Создаётся пользователь и задача, вызывается метод добавления задачи. Проверяется наличие задачи в списке задач пользователя.  

---

### Тест Блочный 2: Отрицательный (Тест добавления дубликата задачи)
**Цель:** Убедиться, что дублирующая задача не добавляется в список задач пользователя.  
**Входные данные:** Пользователь `Анна`, задача `Задача 1`. Два вызова `self.user.add_task(self.task1)`.  
**Ожидаемый результат:** Длина списка задач пользователя остаётся равной 1.  
**Описание процесса:** Добавляем задачу `Задача 1` дважды, проверяем, что она добавляется только один раз и дубликат не сохраняется.  

---

### Тест Блочный 3: Положительный (Тест получения информации о пользователе и его задачах)
**Цель:** Убедиться, что информация о пользователе и его задачах возвращается корректно.  
**Входные данные:** Пользователь `Анна`, задача `Задача 1`. Вызов `self.user.get_info()`.  
**Ожидаемый результат:** Возвращённая информация содержит имя пользователя и описание его задач.  
**Описание процесса:** Добавляем задачу пользователю, вызываем метод получения информации и проверяем, что в выводе содержатся имя пользователя и описание задачи.  

---

### Тест Блочный 4: Положительный (Тест удаления существующей задачи по названию)
**Цель:** Проверить, что задача успешно удаляется из списка задач пользователя по её названию.  
**Входные данные:** Пользователь `Анна`, задача `Задача 1`. Вызов `self.user.remove_task("Задача 1")`.  
**Ожидаемый результат:** Задача `Задача 1` удаляется из списка задач пользователя.  
**Описание процесса:** Добавляем задачу пользователю, удаляем её по названию, проверяем, что задача отсутствует в списке задач пользователя.  

---

### Тест Блочный 5: Отрицательный (Тест удаления несуществующей задачи)
**Цель:** Убедиться, что попытка удалить несуществующую задачу возвращает корректный результат.  
**Входные данные:** Пользователь `Анна`, задача `NonExistingTask`. Вызов `self.user.remove_task("NonExistingTask")`.  
**Ожидаемый результат:** Метод удаления возвращает `False`, список задач остаётся неизменным.  
**Описание процесса:** Пытаемся удалить задачу, которой нет в списке задач пользователя, проверяем, что возвращается `False`, а список задач не изменился.  

# Модуль test_task.py

### Тест Блочный 1: Положительный (Тест получения информации о задаче)
**Цель:** Проверить корректность получения информации о задаче.  
**Входные данные:** Задача `Задача 1`, описание "Описание 1", время "10:00-12:00", местоположение "Офис". Вызов `self.task.get_info()`.  
**Ожидаемый результат:** Возвращённая информация содержит название задачи, описание, время и местоположение.  
**Описание процесса:** Создаём задачу с заданными параметрами, вызываем метод получения информации и проверяем, что все необходимые данные присутствуют в результате.

---

### Тест Блочный 2: Положительный (Тест обновления статуса задачи)
**Цель:** Проверить корректность обновления статуса задачи.  
**Входные данные:** Задача с начальными данными, обновление статуса на "In Progress". Вызов `self.task.update_status("In Progress")`.  
**Ожидаемый результат:** Статус задачи изменяется на "In Progress".  
**Описание процесса:** Создаём задачу, обновляем её статус, проверяем, что статус задачи был изменён на "In Progress".  

---

### Тест Блочный 3: Положительный (Тест обновления описания задачи)
**Цель:** Убедиться, что описание задачи корректно обновляется.  
**Входные данные:** Задача с начальным описанием "Описание 1", обновление описания на "Описание 2". Вызов `self.task.update_description("Описание 2")`.  
**Ожидаемый результат:** Описание задачи изменяется на "Описание 2".  
**Описание процесса:** Создаём задачу с первоначальным описанием, обновляем его, проверяем, что новое описание задачи соответствует ожиданиям.  

---

### Тест Блочный 4: Положительный (Тест обновления местоположения задачи)
**Цель:** Проверить, что местоположение задачи обновляется корректно.  
**Входные данные:** Задача с местоположением "Офис", обновление местоположения на "Дом". Вызов `self.task.update_location("Дом")`.  
**Ожидаемый результат:** Местоположение задачи изменяется на "Дом".  
**Описание процесса:** Создаём задачу с указанным местоположением, обновляем его на новое значение, проверяем, что местоположение изменилось.  

---

### Тест Блочный 5: Положительный (Тест обновления времени задачи на корректное значение)
**Цель:** Проверить, что время задачи обновляется на корректное значение.  
**Входные данные:** Задача с временем "10:00-12:00", обновление времени на "10:00-11:00". Вызов `self.task.update_time("10:00-11:00")`.  
**Ожидаемый результат:** Время задачи изменяется на "10:00-11:00".  
**Описание процесса:** Создаём задачу с заданным временем, обновляем его на новое значение, проверяем, что время изменилось на ожидаемое значение.  

---

### Тест Блочный 6: Отрицательный (Тест обновления времени на некорректное значение)
**Цель:** Проверить, что некорректное время не может быть установлено для задачи.  
**Входные данные:** Задача с временем "10:00-12:00", обновление времени на различные некорректные значения. Вызов `self.task.is_valid_time()`.  
**Ожидаемый результат:** Метод `is_valid_time()` должен возвращать `False` для некорректных значений.  
**Описание процесса:** Проверяем несколько некорректных значений времени и убеждаемся, что метод `is_valid_time` возвращает `False` для всех них. Также проверяем корректное значение, которое должно вернуть `True`.  

---

### Тест Блочный 7: Положительный (Тест обновления всех параметров задачи)
**Цель:** Проверить обновление всех параметров задачи (статус, описание, время, местоположение) одновременно.  
**Входные данные:** Задача с начальными данными. Вызов `self.task.update_all("Completed", "New Description", "15:00-16:00", "Home")`.  
**Ожидаемый результат:** Все параметры задачи обновляются на указанные значения.  
**Описание процесса:** Создаём задачу с начальными значениями, обновляем все её параметры с помощью метода `update_all()`, проверяем, что все параметры задачи изменились на ожидаемые.  

# Модуль test_integration.py

### Тест Интеграционный 1: Положительный (Проверка добавления пользователя и задачи)
**Цель:** Проверить корректность добавления пользователя и задачи.  
**Входные данные:** Добавление пользователя "Алиса", создание задачи "Задачка" с описанием "Описание для задачки". Вызов `add_user("Алиса")`, `user.add_task(task)`.  
**Ожидаемый результат:** Пользователь "Алиса" добавлен в список, задача добавлена в его список задач. Длина списка задач пользователя должна быть равна 1, а название задачи — "Задачка".  
**Описание процесса:** Создаём пользователя и задачу, привязываем задачу к пользователю и проверяем, что задача успешно добавлена в список задач пользователя.

---

### Тест Интеграционный 2: Положительный (Проверка удаления пользователя вместе с его задачами)
**Цель:** Проверить удаление пользователя и всех его задач.  
**Входные данные:** Добавление пользователя "Чарли", создание задачи "Задача" с описанием "Очередная, ничего нового". Вызов `remove_user("Чарли")`.  
**Ожидаемый результат:** Пользователь "Чарли" и его задача должны быть удалены. После удаления пользователь не должен быть найден в списке пользователей, а список пользователей должен быть пуст.  
**Описание процесса:** Добавляем пользователя и задачу, затем удаляем пользователя. Проверяем, что пользователь удалён из списка, и задачи также исчезают.

---

### Тест Интеграционный 3: Положительный (Проверка получения списка пользователей и их задач)
**Цель:** Проверить получение списка всех пользователей и их задач.  
**Входные данные:** Добавление пользователя "Ева", создание задачи "Важная Задача" с описанием "Сделать как можно быстрее". Вызов `get_userlist()`.  
**Ожидаемый результат:** Функция `get_userlist()` должна вернуть список пользователей, а также задачи, привязанные к ним.  
**Описание процесса:** Добавляем пользователя с задачей и вызываем функцию получения списка пользователей. Проверяем, что результат не пустой.

---

### Тест Интеграционный 4: Положительный (Проверка обновления информации о задаче)
**Цель:** Проверить обновление информации о задаче.  
**Входные данные:** Добавление пользователя "Диана", создание задачи "Новая задача" с описанием "Описание". Вызов `task.update_status("Выполняется")`, `task.update_description("Обновлённое описание")`.  
**Ожидаемый результат:** Статус задачи должен быть обновлён на "Выполняется", а описание задачи — на "Обновлённое описание".  
**Описание процесса:** Создаём задачу для пользователя, обновляем её статус и описание, проверяем, что все изменения были успешно применены.

---

# Тест Аттестационный 1: Положительный.
#### **Цель тестирования**:
Проверка корректности работы всех модулей и функций приложения путем ручного выполнения операций пользователем.

### 1. Подготовка к тестированию

1.1. Убедиться, что все модули программы загружены и доступны для тестирования: `main.py`, `usermanager.py`, `user.py`, `task.py`.  
1.2. Запустить программу, убедиться, что меню отображается корректно.

### 2. Сценарии тестирования

#### **2.1. Тестирование добавления пользователя**

- **Шаги:**
    1. Выбрать пункт меню `1. Добавить пользователя`.
    2. Ввести имя пользователя (например, "Иван").
    3. Проверить, что программа подтверждает добавление пользователя.
- **Ожидаемый результат:**
    - Пользователь успешно добавлен.
    - Если имя пустое или дублируется, выводится соответствующее сообщение.

#### **2.2. Тестирование удаления пользователя**

- **Шаги:**
    1. Выбрать пункт меню `2. Удалить пользователя`.
    2. Ввести имя существующего пользователя (например, "Иван").
    3. Повторить с именем несуществующего пользователя.
- **Ожидаемый результат:**
    - Пользователь успешно удален.
    - При вводе несуществующего пользователя отображается сообщение об ошибке.

#### **2.3. Тестирование создания задачи**

- **Шаги:**
    1. Выбрать пункт меню `3. Создать задачу`.
    2. Ввести имя пользователя, которому будет назначена задача (например, "Иван").
    3. Ввести данные задачи:
        - Название: "Задача 1".
        - Описание: "Описание задачи".
        - Время выполнения: "10:00-12:00".
        - Место выполнения: "Офис".
    4. Проверить отображение задачи.
- **Ожидаемый результат:**
    - Задача добавлена к указанному пользователю.
    - При некорректных данных (например, неправильный формат времени) программа запрашивает повторный ввод.

#### **2.4. Тестирование обновления задачи**

- **Шаги:**
    
    1. Выбрать пункт меню `4. Обновить задачу`.
    2. Ввести имя пользователя (например, "Иван").
    3. Выбрать задачу из списка.
    4. Обновить параметры задачи:
        - Статус: "Выполнено".
        - Описание: "Новое описание".
        - Время выполнения: "13:00-15:00".
        - Место выполнения: "Дома".
    
    - Протестировать отдельное обновление каждого параметра.
- **Ожидаемый результат:**
    - Обновленные данные отображаются корректно.
    - Ошибки ввода корректно обрабатываются.

#### **2.5. Тестирование удаления задачи**

- **Шаги:**
    1. Выбрать пункт меню `5. Удалить задачу`.
    2. Ввести имя пользователя (например, "Иван").
    3. Выбрать задачу из списка для удаления.
    4. Повторить для несуществующей задачи.
- **Ожидаемый результат:**
    - Удаление задачи подтверждается.
    - При попытке удаления несуществующей задачи программа выводит сообщение об ошибке.

#### **2.6. Тестирование вывода списка пользователей и задач**

- **Шаги:**
    1. Выбрать пункт меню `6. Вывести список пользователей и задач`.
- **Ожидаемый результат:**
    - Список всех пользователей и их задач отображается корректно.
    - Если данные отсутствуют, программа выводит сообщение "Список пользователей пуст".

#### **2.7. Тестирование выхода из программы**

- **Шаги:**
    1. Выбрать пункт меню `7. Выход`.
- **Ожидаемый результат:**
    - Программа завершается.

### 3. Общие проверки

- Корректность обработки пустых или некорректных вводов (например, пустое имя пользователя, неправильный формат времени).
- Корректность обновления данных в реальном времени (например, удаление пользователя с задачами).
- Вывод информативных сообщений для пользователя.

### 4. Результаты и отчетность

4.1. Заполнить таблицу результатов тестирования:

|**Сценарий**|**Результат (успех/неудача)**|**Комментарий**|
|---|---|---|
|Добавление пользователя|Успех||
|Удаление пользователя|Успех||
|Создание задачи|Успех||
|Обновление задачи|Успех||
|Удаление задачи|Успех||
|Вывод списка пользователей|Успех||
|Выход из программы|Успех||

4.2. Указать замечания и рекомендации в случае ошибок.
