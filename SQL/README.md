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


## Migrations
