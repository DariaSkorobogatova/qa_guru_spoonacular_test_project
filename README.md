<h2> Проект по тестированию UI и API Spoonacular 
<h2> С помощью Spoonacular можно выбирать и создавать рецепты, планы питания, управлять списком покупок и многое другое </h2>

> <a target="_blank" href="https://spoonacular.com/">Ссылка на сайт</a>
![This is an image](design/image/spoonacular.png)


<h3> Список проверок, реализованных в автотестах:</h3>

### UI-тесты
- [x] Проверка заголовков и url на главной странице
- [x] Авторизация пользователя на сайте (успешная и неуспешная)
- [x] Запрос на отправку ссылки на восстановление пароля
- [x] Неуспешная регистрация без капчи
- [x] Добавление и удаление кастомной еды

### API-тесты
- [x] Получение username и hash для юзера
- [x] Отправка запроса неавторизованным пользователем (без ключа, с несуществующим ключом)
- [x] Поиск рецепта по ингредиенту (в т.ч. несуществующему)
- [x] Получение инфо по ингредиенту (в т.ч. по невалидному id)
- [x] Расчет гликемического индекса
- [x] Создание плана меню (на день, на неделю, с ограничением калорий)
- [x] Расчет гликемического индекса
- [x] Поиск рецепта (в т.ч. поиск похожего рецепта)
- [x] Добавление и удаление из списка покупок

## Структура проекта
### Проект реализован с использованием
|                                      Python                                       |                                      Pytest                                       |                                       PyCharm                                       |                                   Selene                                    |                                       Jenkins                                       |                              Allure Report                               |                                      Allure TestOps                                      |                                   Telegram                                   |
|:---------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| <img src="/design/icons/python-original.svg" alt="Python" width="45" height="45"> | <img src="/design/icons/pytest-original.svg" alt="Pytest" width="45" height="45"> | <img src="/design/icons/intellij_pycharm.png" alt="Pycharm" width="45" height="45"> |  <img src="/design/icons/selene.png" alt="Selene" width="45" height="45">   | <img src="/design/icons/jenkins-original.svg" alt="Jenkins" width="45" height="45"> | <img src="/design/icons/allure.png" alt="Allure" width="45" height="45"> | <img src="/design/icons/allure_testops.png" alt="Allure TestOps" width="45" height="45"> | <img src="/design/icons/telegram.svg" alt="Telegram" width="45" height="45"> |


## Локальный запуск автотестов
### Для локального запуска с дефолтными значениями необходимо выполнить команду:
```
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest tests
```

## Удаленный запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/spoonacular_test_project/">Ссылка на проект в Jenkins</a>

### Для запуска автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/spoonacular_test_project/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Указать комментарий
4. Нажать кнопку `Build`
5. Результат запуска сборки можно посмотреть в отчёте Allure

----
### Allure отчет


#### Общие результаты

#### Список тест кейсов

#### Пример отчета о прохождении ui-теста
![This is an image](design/image/ui_test_example.png)
#### Пример отчета о прохождении api-теста
![This is an image](design/image/api_test_example.png)

----
### Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/4097/dashboards">Ссылка на проект в AllureTestOps</a> (запрос доступа `admin@qa.guru`)

#### Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)
![This is an image](design/image/test_ops_testcases.png)

#### Пример отчёта выполнения одного из автотестов
![This is an image](design/image/test_ops_example_test.png)

#### Тестовые артефакты
![This is an image](design/image/test_ops_artefacts.png)

#### Пример dashboard с общими результатами тестирования
![This is an image](design/image/dashboard.png)

#### История запуска тестовых наборов
![This is an image](design/image/launch_history.png)

----
### Оповещение о результатах прогона тестов в Telegram
![This is an image](design/image/tg_notification.png)

----
### Пример видео прохождения ui-автотеста
![autotest_gif](design/image/test.gif)

