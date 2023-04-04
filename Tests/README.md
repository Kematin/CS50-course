- [Testing](#Testing)
- [Assert](#Assert)
  - [Test-Driven Development](#TestDriven)
- [Unit Testing](#UnitTest)
- [Django Testing](#DjangoTest)
- [Client Testing](#ClientTest)
- [Selenium](#Selenium)

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
