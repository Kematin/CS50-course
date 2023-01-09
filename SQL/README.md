# SQL, MODELS and MIGRATIONS

- [SQL](#SQL)
    - [Data](#Data)
    - [Tables](#Tables)
    - [Add data in tables](#Add)
    - [SQL Queries](#Queries)
        - [Update](#UPDATE)
        - [Delete](#DELETE)
        - [Other clauses](#Other)
    - [Join tables](#Join)
    - [Create Index](#INDEX)
    - [SQL Vulnerabilities](#Vulnerabilities)
        - [SQL Injection](#Injection)
        - [Race condition](#Race-Condition)
- [Django Models](#Models)
    - [Django Migrations](#Migrations)
    - [Django Shell](#Shell)
        - [Merging tables by Python](#Merging)
        - [Display information on site](#Display)
        - [More shell commands](#Commands)
- [Django Admin](#Admin)
    - [Display more info about object](#DisplayRout)
- [Many-to-Many Relationships](#Many-to-Many)
- [Add passengers in flight](#Passengers)

## SQL

### Data

Базы данных делятся на 2 типа:
- Реляционные (SQL)
- Не реляционные (NoSQL)

***Реляционные*** базы данных состоят из столбцов и строк в строгой конструкции, 
где данные будут расположены организационно. 

<table>
    <tr>
        <th>Origin</th>
        <th>Destination</th>
        <th>Duration</th>
    </tr>
    <tr>
        <td>New York</td>
        <td>London</td>
        <td>415</td>
    </tr>
    <tr>
        <td>Istanbul</td>
        <td>Tokio</td>
        <td>800</td>
    </tr>
    <tr>
        <td>Moscow</td>
        <td>Paris</td>
        <td>250</td>
    </tr>
</table>

Такие базы данных регулируются специальными системами-языками 
(Database Management Systems)

Наиболее популярные SQL языки:
- PostgreSQL[^P]
- MySQL[^M]
- SQLite[^L]

Каждые из них имеют свои особенности, которые можно использовать на проектах разного
типа, уровня. 

[^P]:Например Postgres (PostgreSQL) более тяжелая система, которая 
надежно обрабатывает большое количество данных и именно её чаще используют на крупных
проектах.

[^M]:MySQL же не такая надежная система, но более быстрая и универсальная, что 
позволяет ее использовать на многих проектах.

[^L]:SQLite легкая система, в которой можно быстро разобраться и используется на 
маленьких проектах ведь все данные можно хранить в одном файле.


Базы данных, как и языки программирования имеют свои типы данных. Если в Python
например есть bool, integer, string и т.д. то например SQLite имеет такой
короткий список тип данных:
- **TEXT** (Текст)
- **NUMERIC** (Для особенных последовательности чисел, например дни рождения 2.10.2020)
- **INTEGER** (Действительные числа -10, 0, 5 и т.д.)
- **REAL** (Числа с плавающей точкой 4.5, -2.1, 0.42 и т.д.)
- **BLOB** (Какой либо бинарные объект)


### Tables
Для создания базы данных надо создать таблицу и команда для создания будет выглядеть 
примерно так (_SQLite_):

```bash
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL,
);
```

**1.** Командой CREATE TABLE создается таблица с именем flights.<br>
**2.** Далее идут какие столбцы будут в таблице (4: id, origin, destination, duration).<br>
**3.** Каждя таблица должна содержать столбец где будут уникальные ключи для каждой строки - id.<br>
**4.** Вместе с названием столбцов вторым аргументом идет тип данных в столбцах.<br>
**5.** Третий аргумент (Constraints) в id означает что это столбец с уникальными ключами для оптимизации процесса.<br>
**6.** NOT NULL означает что значения в строках данных столбцов не может быть пустым.<br>
**7.** AUTOINCREMENT означает что уникальный ключ будет создаваться с каждым добавлением новой строки.

Виды Constraints в SQLite:
- **CHECK**
- **DEFAULT**
- **NOT NULL** (Значение не может быть пустым)
- **PRIMARY KEY** (Особый ключ id)
- **UNIQUE** (Гарантирует что каждое значение будет уникальным)
- **...**

### Add

Для добавления данных в таблицу используется команда **INSERT** с интуитивно понятным
синтаксисом:

```
INSERT INTO flights 
    (origin, destination, duration)
    VALUES ("New York", "London", 415);
```
_Значение id не добавляется вручную т.к. мы указали его как автозаполнение._

### Queries

Для того чтобы взять значения с таблиц используется команда **SELECT**:

```
1 - SELECT * FROM flights;
2 - SELECT origin, destination FROM flights;
```
1. Этой командой мы берем абсолютно все данные с таблицы.
2. Второй командой мы берем данные лишь с столбцов origin, destination.

Так-же чтобы не брать тысячи строк значений с одного столбца, командой **WHERE**
можно профильтровать выборку значений:

```
1 - SELECT * FROM flights WHERE id = 3;
2 - SELECT * FROM flights WHERE origin = "New York";
3 - SELECT * FROM flights WHERE duration > 300 AND origin = "Paris"
4 - SELECT * FROM flights WHERE duration > 200 OR origin = "New York"
5 - SELECT * FROM flights WHERE origin IN ("New York", "Paris", "London")
6 - SELECT * FROM flights WHERE origin LIKE "%b%"
```
1. Этой командой мы берем данные строки где id = 3.
2. Этой командой мы берем данные строки где origin имеет значение New York.
3. Этой командой мы берем данные строки где origin имеет значение Paris и duration больше 300.
4. Этой командой мы берем данные строки где origin имеет значение New York или duration больше 200.
5. Команда как in в python.
6. Этой командой мы берем данные строки где в origin есть буква b.

#### UPDATE

Команда **UPDATE** нужна для изменения какого либо параметра в базе данных

```
UPDATE flights
    SET duration = 450
    WHERE origin="New York" AND destination="Moscow";
```
Меняет значение duration на 450 по нижним условиям.

#### DELETE

Команда удаляет строку(и) из базны данных по условиям

```
DELETE FROM flights 
    WHERE id IN (1, 5);
```
Удаляет 1 и 5 строку из базы данных.


#### Other
Класс это:<br>
SELECT * FROM flights `class` `requirement`

- **LIMIT** (до какого номера строки)
- **ORDER BY** (выдавать данные по признаку столбца)
- **GROUP BY** (группировать выдачу данных по столбцу)
- ...

### Join

Базы данных состоят из большого кол-ва таблиц и для удобства их использования 
их можно объеденять с помощью join.

Команда для использования JOIN:
```
SELECT row_name_1, row_name_2, row_name_n
    FROM table_name JOIN table_name_2
    ON table_name_2.row_name_id = table_name.id;
```

Пример:
```
SELECT first, origin, destination 
    FROM flights JOIN passengers
    ON passengers.flight_id = flights.id;
```
Берет значения first, origin, destination из таблицы flights 
и вставляет эти значения сопоставляя flight_id из passengers и id из flights

**JOINs**
- JOIN / INNER JOIN
- LEFT OUTER JOIN
- RIGHT OUTER JOIN
- FULL OUTER JOIN

### INDEX

Позволяет повысить производительность запросов (подобно индексу в конце учебника).<br>
_*Примечание: при обновление таблицы, INDEX так-же надо обновлять, поэтому 
скорость обновления таблиц уменьшается_

Команда INDEX:
```
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

### Vulnerabilities

#### Injection

***SQL Injection*** - самая популярная уязвимость. 
Это внедрение SQL кода в запросе на сайте, который вы неосознанно обрабатываете на 
сервере.

**Пример**:<br>
У Джона логин king и пароль 12345. При поступление данных наш запрос будет выглядеть 
так:
```
SELECT * FROM users;
    WHERE username = "king" AND password = "12345"
```
Но хакер может поставить `--` вместо пароля, ведь данный прочерк означает комментарий
и обрабатываться запрос будет так (т.е. хакер получит доступ к аккаунту Джона):
```
SELECT * FROM users;
    WHERE username = "king" -- AND password = "12345"
```

Данную проблему можно решить 2 способами:
- Обрабатывать вводимые данные и проверять их на то, являются ли они SQL кодом.
- Добавить абстрактный слой перед SQL запросами, чтобы самостоятельно их не создавать.

#### Race-Condition

***Race Condition*** или "или состояние гонок" еще одна проблема, нарушающая один 
из принципов ACID - Isolation (изоляция), когда на транзакцию одного юзера накладывается
транзакция чужого юзера тем самым ошибочно работая с данными 2-ого юзера как с первым.
[Видео Over Enginerr на эту тему](https://www.youtube.com/watch?v=gOB3hpAVIIQ&t=818s)


## Models

**Django Models** - Абстрактный слой выше SQL, позволяющий работать нам с базами данных
с помощью классов и обьектов, а не напрямую запросами.

Модели создаются в файле `models.py` в директории приложения. В классе нашей модели
мы описываем какие данные будут использоваться в приложении.

Пример:
```python
class Flights(models.Model):
    origin = models.CharField(max_length = 50)    
    destination = models.CharField(max_length = 50)    
    duration = models.IntegerField()
```

1. Первой строкой создается модель, наследующая дефолтную модель Джанги
2. Далее создаются поля для данных: origin, destination, duration
3. В аргументе 2 полей ограничевается максимальная длина


### Migrations

Теперь, когда созданна модель надо создать базу данных из модели. Делается это 
командой:

`python manage.py makemigrations`

Данная команда создает `файл` в папке `migrations` благодаря которому можно редактировать
или создавать базы данных исходя из модели.

Далее, командой ниже мигрируется наша модель, дефолтные модели джанго и создается
база данных (sqlite3 по умолчанию):

`python manage.py migrate`

### Shell

Работать с базой данной с помощью пайтон команд можно через Django Shell оболочку.

`python manage.py shell`

Пример работы в shell:
```python
# Import flight model
from flights import Flight

# Create a new flight
f = Flight(origin="New York", destination="London", duration=400)

# Save information in db
f.save()

# Query for all flights stored in the database
In [4]: Flight.objects.all()
Out[4]: <QuerySet [<Flight: Flight object (1)>]>
```

Для того чтобы вывод объектов был более информативен создается магический метод `__str__`
```python
class Flights(models.Model):
    origin = models.CharField(max_length = 50)    
    destination = models.CharField(max_length = 50)    
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```

```python
In [4]: Flight.objects.all()
Out[4]: <QuerySet [<Flight: 1: New York to London>]>
```

Пример работы в shell c объектами базы данных:
```python
# Import flight model
from flights.models import Flight

# Get last element from db (also can get first element)
last_flight = Flight.objects.all().last()

# Display element
In [3]: last_flight
Out[3]: <Flight: 2 --- New York --- London --- 415>

# Display origin and destination from object
# (Referring to an element as an attribute in classes)
In [4]: last_flight.origin, last_flight.destination
Out[4]: ('New York', 'London')
```

#### Merging

```python
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
        

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```

1. Создается новая модель, а во второй CharField заменяется ForeignKey,
означающий, что данные будут заменятся от другой модели.
2. Первый аргумент ForeignKey означает с какой модели будут интегрироваться данные.
3. Второй аргумент означает логику при удалении данных из интегрируемой модели 
(CASCADE - полное удаление данных в модели). Другие типы данного аргумента в 
[статье](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.ForeignKey.on_delete).
4. Третий аргумент это связанное имя по которому можно быстро найти данные.


**Shell**:
```python
# Import all models
In [1]: from flights.models import *

# Create some new airports
In [2]: jfk = Airport(code="JFK", city="New York")
In [4]: lhr = Airport(code="LHR", city="London")
In [6]: cdg = Airport(code="CDG", city="Paris")
In [9]: nrt = Airport(code="NRT", city="Tokyo")

# Save the airports to the database
In [3]: jfk.save()
In [5]: lhr.save()
In [8]: cdg.save()
In [10]: nrt.save()

# Add flight and save in db 
In [11]: f = Flight(origin=cdg, destination=nrt, duration=515)
In [12] f.save()

# Display some info about the flight
In [13]: flights = Flight.objects.all()
In [14]: flight = flights[0]
In [15]: fligh.destination
Out[15]: <Airport: Tokyo (NRT)>

# Using the related name to query by airport of arrival:
In [16]: nrt.arrivals.all()
Out[16]: <QuerySet [<Flight: 1 --- Paris (CDG) --- Tokyo (NRT) --- 515>]>
```

#### Display

`urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
```

`views.py`
```python
from django.shortcuts import render
from .models import Airport, Flight

def index(request):
    context = {
            "airports": Airport.objects.all(),
            "flights": Flight.objects.all(),
        }
    return render(request, "index.html", context)
```

`templates/layout.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flights</title>
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```

`templates/index.html`
```html
{% extends "layout.html" %}

{% block body %}
    <h1>Airports:</h1>
    <ul>
        {% for airport in airports %}
            <li>Airport: {{ airport.id }}: {{ airport.city }} ({{ airport.code }})</li>
        {% endfor %}
    </ul>
    <h1>Flights</h1>
    <ul>
        {% for flight in flights %}
            <li>Flight: {{ flight.id }}: {{ flight.origin }} to {{ flight.destination }} ({{ flight.duration }} minutes)</li>
        {% endfor %}
    </ul>
{% endblock %}
```


#### Commands

**Shell**

```python
# Using the filter command to find all airports based in New York
In [3]: Airport.objects.filter(city="New York")
Out[3]: <QuerySet [<Airport: New York (JFK)>]>

# Using the get command to get only one airport in New York
In [5]: Airport.objects.get(city="New York")
Out[5]: <Airport: New York (JFK)>

# Assigning some airports to variable names:
In [6]: jfk = Airport.objects.get(city="New York")
In [7]: cdg = Airport.objects.get(city="Paris")

# Creating and saving a new flight:
In [8]: f = Flight(origin=jfk, destination=cdg, duration=435)
In [9]: f.save()
```

## Admin

Что-бы добавлять новые объекты ранее использовался shell, этот процесс можно 
упростить с помощью админки. Для начала создается супер юзер (админ)

```
/mnt/d/CS50/SQL/airline (main*) » python manage.py createsuperuser
Username (leave blank to use 'kematin'): user_1
Email address: a@inbox.ru
Password: 
Password (again): 
```

Теперь надо добавить модели в админ панель.

`admin.py`
```python
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Flight)
admin.site.register(Airport)
```

На сайте перейдя по адресу `/admin` теперь можно войти в админ панель, откуда 
можно манипулировать данными.

### DisplayRout
Отображение большей информации насчет полета (для каждого отдельный путь)

`views.py`
```python
# Function, which return html template
def flight(request, flight_id):
    # Get info about flight by id
    flight = Flight.objects.all().get(id=flight_id)
    context = {
            "flight": flight,
        }
    return render(request, "flight.html", context)
```

`urls.py`
```python
# Append new route with variable flight id
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:flight_id>', views.flight, name="flight"),
]
```

`template/flight.html`
```html
<!-- Create template, which display info -->
{% extends 'layout.html' %}

{% block body %}
    <h1>Flight {{ flight.id }}</h1>
    <ul>
        <li>Origin - {{ flight.origin }}</li>
        <li>Destination - {{ flight.destination }}</li>
        <li>Duration - {{ flight.duration }}</li>
    </ul>
    <a href="{% url 'index' %}">All Flights</a>
{% endblock %}
```

## Many-to-Many
Реализация отношения многие к многим через добавление новой модели:

`models.py`
```python
# Create new model
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passenger")

    def __str__(self):
        return f"{self.first} {self.last}"
```

1. ManyToManyField и Flight (первым аргументом) означает что данное поле будет в отношение многим к многим с 
таблицей (моделью) Flight
2. blank=True означает что значение полета у пассажира может быть None.

Отображение на странице сайта

`views.py`
```python
# Create function, which get all passengers from flight
def flight(request, flight_id):
    flight = Flight.objects.all().get(id=flight_id)
    passengers = flight.passengers.all()
    context = {
            "flight": flight,
            "passengers": passengers,
        }
    return render(request, "flight.html", context)
```

`flight.html`
```html
{% extends 'layout.html' %}

<!-- Display elements on site -->
{% block body %}
    <h1>Flight {{ flight.id }}</h1>
    <ul>
        <li>Origin - {{ flight.origin }}</li>
        <li>Destination - {{ flight.destination }}</li>
        <li>Duration - {{ flight.duration }}</li>
    </ul>
    <h1>Passengers:</h1>
    <ul>
        {% for passenger in passengers %}
            <li>{{ passenger }}</li>
        {% empty %}
            <li>No passengers.</li>
        {% endfor %}
    </ul>
    <a href="{% url 'index' %}">All Flights</a>
{% endblock %}
```


### Passengers

Добавление пассажиров в полет:

Для лучшего понимания лучше изобразить цикличную схему в последовательности:
1. Объект Flight
2. Html форма
3. Функция book

`urls.py`
```python
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:flight_id>', views.flight, name="flight"),
    # Add new route to add passenger in flight
    path('<int:flight_id>/book', views.book, name="book"),
]
```

`views.py`
```python
def flight(request, flight_id):
    flight = Flight.objects.all().get(id=flight_id)
    passengers = flight.passengers.all()
    # find all passengers, who not in flight
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    context = {
            "flight": flight,
            "passengers": passengers,
            "non_passengers": non_passengers,
        }
    return render(request, "flight.html", context)


def book(request, flight_id):
    # if a post request, add new passenger
    if request.method == "POST":
        
        # accesing flight
        flight = Flight.objects.all().get(id=flight_id)

        # find id passenger from submitted data
        passenger_id = int(request.POST["passengers"])

        # find passenger from based id
        passenger = Passenger.objects.get(pk=passenger_id)

        # add new passenger in flight
        passenger.flights.add(flight)

        # redirect user to flight route
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
```

`flight.html`
```html
    <!-- Create new form, which url is flight/flight_id/book -->
    <form action="{% url 'book' flight.id %}" method="post">
        {% csrf_token %}
        <select name="passengers" id="">
            <!-- Cycle "for" in non_passengers for add this passengers -->
            {% for passenger in non_passengers %}
                <option value="{{ passenger.id }}">{{ passenger }}</option>
            {% empty %}
                All available passengers in flight.
            {% endfor %}
        </select>
        <input type="submit" value="Submit">
    </form>
```
