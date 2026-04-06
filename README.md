markdown

## Описание

Автотесты для формы на сайте https://practice-automation.com/form-fields/

- **Язык:** Python 3.10
- **Фреймворк:** PyTest
- **Инструменты:** Selenium WebDriver, Allure
- **Паттерны:** Page Object Model, Fluent

---

##  Результат Allure отчета
---
<img width="1919" height="1022" alt="Снимок экрана 2026-04-07 002534" src="https://github.com/user-attachments/assets/e2c613fb-000f-4887-843a-4280ceea9c79" />


##  Вывод в командной строке
<img width="1405" height="451" alt="Снимок экрана 2026-04-06 233440" src="https://github.com/user-attachments/assets/f003cf20-1b37-431b-943d-b7b31b21d509" />
##  Тест-кейсы

### TC-01: Позитивный тест заполнения формы

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Открыть страницу | Форма загружена |
| 2 | Заполнить поле Name = "John" | Поле заполнено |
| 3 | Заполнить поле Password = "1234" | Поле заполнено |
| 4 | Выбрать Milk и Coffee | Чекбоксы отмечены |
| 5 | Выбрать Yellow | Радиокнопка выбрана |
| 6 | Выбрать Automation = "Yes" | Опция выбрана |
| 7 | Заполнить Email = "name@example.com" | Поле заполнено |
| 8 | Заполнить Message = "4 Selenium WebDriver" | Поле заполнено |
| 9 | Нажать Submit | Форма отправлена |
| 10 | Проверить alert | Alert "Message received!" |

**Статус:** ✅ PASSED


---

### TC-02: Негативный тест (обязательные поля)

| Шаг | Действие | Ожидаемый результат |
|-----|----------|---------------------|
| 1 | Открыть страницу | Форма загружена |
| 2 | Заполнить только поле Name | Другие поля пустые |
| 3 | Нажать Submit | Валидация не пропускает |
| 4 | Проверить alert | Alert отсутствует |

**Статус:** ✅ PASSED

---

Запуск автотестов

### Установка зависимостей

```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
2. Запуск тестов
bash
pytest tests/test_form.py -v
3. Генерация Allure отчета
bash
pytest tests/test_form.py --alluredir=allure-results -v
allure serve allure-results
Структура проекта
text
sdet-project/
├── tests/
│   ├── __init__.py
│   └── test_form.py          # Тест-кейсы
├── pages/
│   ├── __init__.py
│   └── form_page.py          # Page Object
├── conftest.py                # Фикстуры
├── requirements.txt           # Зависимости
├── README.md                  # Документация
└── allure-screenshot.png      # Скриншот отчета
🛠 Использованные селекторы
Элемент	Тип	Значение
Name	ID	name-input
Password	CSS	input[type='password']
Milk	ID	drink1
Coffee	ID	drink2
Yellow	ID	color4
Automation	ID	automation
Email	ID	email
Message	ID	message
Submit	ID	submit-btn
Использованы: CSS, XPath, ID

