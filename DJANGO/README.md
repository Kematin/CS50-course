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
