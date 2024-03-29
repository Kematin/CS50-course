- [Testing](#testing)
- [Assert](#assert)
	- [TestDriven](#testdriven)
- [UnitTest](#unittest)
- [DjangoTest](#djangotest)
- [ClientTest](#clienttest)
- [Selenium](#selenium)
- [CI/CD](#cicd)
- [Auctions](#auctions)
- [Docker](#docker)

# Testing

Одно из важных направлений в программирование - это тестирование. Благодаря
тестам можно найти уязвимые места в программе

# Assert

Один из простейших способов протестировать код - использовать `assert`.
Пример его использования в [assert.py](assert.py)

## TestDriven

Когда вы начнете создавать более крупные проекты, возможно,
вы захотите рассмотреть возможность использования тестовой разработки -
стиля разработки, при котором каждый раз, когда вы исправляете ошибку,
вы добавляете тест, проверяющий наличие этой ошибки, в растущий набор тестов,
которые запускаются каждый раз, когда вы вносите изменения. Это поможет вам
убедиться в том, что дополнительные функции, которые вы добавляете в проект,
не будут мешать существующим функциям.

Пример такого подхода в [driven.py](driven.py)

# UnitTest

Unit Тестирование - это тестирование отдтельно взятых блоков кода `юнитов` (функций, классов и т.д.)

Пример юнит тестирования в файле [unit.py](unit.py)

Вывод о ошибках юнит тестов:

```bash
Display success and false tests
...F.F

Show faled test and commentary from docstring
======================================================================
FAIL: test_25 (__main__.Tests)
Check that 25 is not prime.

Display error
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests1.py", line 26, in test_25
    self.assertFalse(is_prime(25))
AssertionError: True is not false
```

# DjangoTest

Для создания тестов django, существует модуль tests.py.

Пример по созданию тестов:

```python
from django.test import TestCase
from .models import Model

# Create your tests here.
class MainTestCase(TestCase):

    # Create some entries for tests
    def setUp(self) -> None:
        # create some data for tests
        a1 = Model.objects.create(name="a1", value=3)
        a2 = Model.objects.create(name="a2", value=1)

    # Tests
    def test_departures_count(self):
        """This test checks valid of first value"""
        a = UseFul.objects.get(name="a1")
        self.assertEqual(a.value, 3)

    def test_arrivals_count(self):
        """This test checks valid of second value"""
        a = UseFul.objects.get(name="a2")
        self.assertEqual(a.value, 1)
```

Для запуска тестов используется команада:

`./manage.py test`

Вывод в консоль такой же как при юнит тестах.

Более полный пример в приложение [testing](tests_project/testing) проекта **tests_project**.

# ClientTest

Так-же важно тестировать функции, выполнения которых зависит от клиента, а не
от работы сервера (функция при нажатии на кнопку, скроллинг, загрузка страницы и т.д.).

Для этого в джанго есть модуль `Client` из пакета `django.test`.

Более полный пример в приложение [testing](tests_project/testing) проекта **tests_project**.

# Selenium

Selenium - инструмент для тестирование клиентской стороны приложения (тестирование буквально в браузере).
Помогает отлавливать ошибки при взаимодействие с веб сайтом.

Пример тестирования с помощью Selenium в файле [selenium_test.py](selenium_test.py)

# CI/CD

**CI/CD**, что расшифровывается как **Continuous Integration and Continuous Delivery**,-
это набор лучших практик разработки программного обеспечения, которые определяют,
как код пишется командой людей и как этот код впоследствии доставляется пользователям
приложения. Как следует из названия, этот метод состоит из двух основных частей:

1. Непрерывная интеграция:

- Частое слияние с основной веткой
- Автоматическое модульное тестирование при каждом слиянии

2. Непрерывная поставка:

- Короткие графики выпуска, то есть новые версии приложения выпускаются часто.

CI/CD становится все более популярным среди команд разработчиков программного обеспечения по ряду причин:

- Когда разные члены команды работают над разными функциями, может возникнуть множество проблем совместимости при одновременном объединении нескольких функций. Непрерывная интеграция позволяет командам решать небольшие конфликты по мере их возникновения.
- Поскольку модульные тесты запускаются при каждом слиянии, в случае сбоя теста легче изолировать часть кода, вызывающую проблему.
- Частый выпуск новых версий приложения позволяет разработчикам изолировать проблемы, если они возникают после запуска.
- Выпуск небольших, постепенных изменений позволяет пользователям постепенно привыкать к новым функциям приложения, а не перегружаться совершенно другой версией.
- Отсутствие ожидания выпуска новых функций позволяет компаниям оставаться впереди на конкурентном рынке.

# Auctions

Один из инструментов неприрывной интеграции является GitHub Auctions.
С помощью него можно автоматически прогонять билды, линтеры, юнит тесты и т.д. перед отправкой
кода в репозиторий. Его принцип заключается в том, что он не позволяет коду оказаться
в репозитории если он не прошел все проверки.

Для настройки Auctions используются простые YAML файлы со структурой key-value

```yaml
key1: value 1
key2: value 2
key3:
  - item 1
  - item 2
  - item 3
```

Чтобы гитхаб принимал тесты создается каталог `.github` c подкаталогом `workflows`. И в
данном подакаталоге создать файле с расширением yaml.

Пример:

> REPO_DIR/.github/workflows/test.yaml

```yaml
name: Testing
on: push

jobs:
  test_project:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Linters
        run: echo "TODO linters"
      - name: Run Django unit tests
        run: echo "TODO unit tests"
```

[Подробное объяснение каждой строчки](https://cs50.harvard.edu/web/2020/notes/7/#github-actions)

# Docker

Часто случается так, что каждое приложение имеет свою версию языка, или разные
библиотеки. Если запускать множество таких приложений на сервере, то он может
крашнуться от несовместимости версий, или перегруженности.

Данную проблему решает docker. С помощью него можно создать отдельный **контейнер**,
в котором будет билд приложения (версия языка, библиотеки и т.д.). Так-же данными
контейнерами можно делится и запускать в _один клик_, что крайне упращает процесс
сборки.

По сути docker - это способ разгроничения памяти в качестве хоста, в который
входит сеть, юзер, ipc, mount и т.д. Docker изолирует процесс в рамке
машины (main host`а).

_Docker Image_ - образ докер контейнера.

[Установка](https://docs.docker.com/get-docker/)

Работа с докер:

```bash
# Create simple container
docker run hello-world

# See all working containers
docker ps

# See all docker images
docker images

# Create contanier with template (mongo)
docker run --name=mongo mongo -d

# Run container and stop its
docker start mongo
docker stop mongo

# Restart and delete container (image will not be deleted)
docker restart mongo
docker rm mongo
```
