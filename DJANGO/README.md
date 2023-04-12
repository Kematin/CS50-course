# WEB

**HTTP** or HyperText Transfer Protocole - протокол позволяющий *общаться* серверу и клиенту благодаря запросам.
**HTTPS** более защищенная версия данного протокола.

***Пример 1***[^get]
```
Запрос:
GET / HTTP/1.1
Host: www.example.com
```

***Пример 2***[^answer]
```
Ответ:
HTTP/1.1 200 OK
Content-Type: text/html
```

[^get]: С помощью метода get задаем запрос на получение страницы с версией протокола 1.1.<br>
В строке host, очевидно, находится сервер у которого мы запрашиваем контент.

[^answer]: Ответ от протокола версией 1.1 с кодом 200, означающий что все в порядке.<br>
Во второй строчке тип полученных данных.


## Django

**Django** - фреймворк для языка python, который позволяет добавлять логику веб странице.

### Start using django

1. Создание вертуалки (`python3 -m venv django`)
2. Установка Django (`pip3 install django`)
3. Создания проекта (`django-admin startproject PROJECT_NAME`)

После создания проекта мы увидим данную структуру, пока нас должно интересеровать только manage.py.

- Project
    - Project
        - \_\_init\_\_.py
        - asgi.py
        - settings.py
        - urls.py
        - wsgi.py
    - manage.py

Для начала мы можем запустить наш сервер командой: `python3 manage.py runserver` и перейдя по ссылке
убедиться что наш сервер создан и вполне нормально работает.

После всех этих действий можно создать наше веб приложение на django.<br>
`python manage.py startapp APP_NAME`. Появится данная структура

- APP\_NAME
    - migrations
        - \_\_init\_\_.py
    - \_\_init\_\_.py
    - admin.py
    - apps.py
    - models.py
    - tests.py
    - views.py

Так-же надо добавить наше приложение в настройки django. В файле `settings.py` находим строку
`INSTALLED_APPS` и добавляем в список название нашего приложения.

Пока разберем views.py

### Routes

В Файле views.py будут распологаться все условные маршруты сайта, т.е. то что идет после слеша. 
Например site.ru/page2 или site.ru/hello.

##### Чтобы создать ответвления на нашем сайте нужно выполнить следующие действия.

- Создать файл urls.py в приложении.
- Добавить функцию в views.py.
- Добавить наш файл urls.py в основной, который находится в директории проекта.

##### Как это выглядет в коде

> Project/App/views.py
```python
from django.http import HttpResponse
from django.shortcuts import render

def content(request):
    return HttpResponse("Cool text")
```

> Project/App/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('page1', views.content, name='content')    
]
```

> Project/Project/urls.py
```python
from django.contrib import admin
from django.urls import include, path

# Первый аргумент path это ответвление сайта (site.com/page/page1).
# Второй аргумент это импортирование из директории приложения модуля с именем urls.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/', include('APP_NAME.urls'))
]
```

### Templates

Мы так-же можем имортировать html страницы в наши ссылки и модернизировать их из языка разметки в продвинутый язык[^how-use-code]. Например
добавить переменные. Чтобы это сделать с начало в папке приложения нужно создать директории. 

Это должно выглядеть так:
`APP_NAME/templates/TEMPLATE_NAME/HTML_NAME.html`

И чтобы наша страница отображалась на сайте, надо создать функцию возвращающую данную страницу. 

```python
from django.shortcuts import render

# В первом аргументе мы говорим что должны отправить страницу пришедшему запросу.
# Во втором аргументе указываем путь до страницы.

def content(request):
    return render(request, 'TEMPLATE_NAME/HTML_NAME.html')
```

[^how-use-code]: Как внедрять в html python можно посмотреть в файлах [views.py](./first_project/first_app/views.py), 
[greet.html](./first_project/first_app/templates/hello/greet.html).

Чтобы внедрять css в наши страницы надо создать отдельную папку static файлов, т.к. django 
динамично обрабатывает все файлы в нашей структуре. Должно это выглядеть так:

`APP_NAME/static/FOLDER_NAME/STYLE_NAME.css`

> HTML file
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Site</title>
    <link rel="stylesheet" href="{% static 'FOLDER_NAME/STYLE_NAME.css' %}">
</head>
<body>
    
</body>
</html>
```

## Tasks

### Relative links

В Django чтобы не использовать ссылки напрямую к файлу (что очень неудобно), можно 
использовать ссылки ведущие на страницу в urls.py. Это можно сделать благодаря именам ссылок.

> urls.py
```python
app_name = 'tasks'
urlpatterns = [
    path('add', views.add, name='add_new')
]
```

> File.html
```html
<body>
    <a href="{% url 'tasks:add_new' %}">Add new task</a>
</body>
```

### Method Post

Метод Get означает что мы запрашиваем переход на определенную ссылку. Отправляя же запрос 
Post в нашей ссылке не будут появляться новые значения. Мы отправляем определенные данные
на наш сервер. 

Чтобы защитить свои данные от кражи, следует использовать csrf токен. Создается токен
со случайным значением и после отправки данных, сервер принимает токен и позволяет принять данные.

> File.html
```html
<form action="{% url 'app_name:file' %}" method="post">
    {% csrf_token %}
    <input type="text" name="tasks">
    <input type="submit">
</form>
```

### Form

Что-бы получать данные с форм, надо использовать формы созданные django, благодаря 
им мы можем отправлять данные на сервер. 

> views.py
```python
from django import forms
from django.shortcuts import render

tasks = ['taks 1', 'task 2']
def add(request):
    # Проверяем метод запроса
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            # Берем данные с формы с именем FORM_NAME и добавляем их в список
            task = form.cleaned_data(['FORM_NAME'])
            tasks.append(task)

        else:
            # Возвращаем форму с предупреждением если данные не правильные
            return render(request, 'TEMPLATE_NAME/File.html', {
                'form': form
            })

    # Возвращаем html файл с переменной form
    return render(request, 'TEMPLATE_NAME/File.html', {
        'form': TaskForm()
    })

# Создание формы
class TaskForm(form.Form):
    FORM_NAME = forms.CharField(label="Add New Task")
```

> File.html
```html
<!-- Перезагрузка страницы после получение данных -->
<form action="{% url 'app_name:file' %}" method="post">
    <!-- Создаем токен и вставляем созданную форму из views -->
    {% csrf_token %}
    {{ form }}
    <input type="submit">
</form>
```

### Session

Теперь, добавляя что либо в список задач мы можем увидеть, что каждая новая локальная задача 
будет отображаться на всех устройствах. Чтобы у каждого пользователя была локальная сессия
нужно создать наш список в локальной сессии. Перед этим нужно выполнить данную команду в терминале:

`python3 manage.py migrate`

Как внедрить список в сессию можно посмотреть в файле [views.py](./first_project/tasks/views.py),
в коммите `django: session`

