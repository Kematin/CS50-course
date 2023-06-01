# JavaScript

Так-же существует множество способов атаковать сервер с помощью js. Один из таких примеров - это **Cross-Site Scripting**, когда пользователь может вводить произвольный код для сайта. Для пример у нас есть такое приложение на django:

```python
urlpatterns = [
    path("<path:path>", views.index, name="index")
]
```

```python
def index(request, path):
    return HttpResponse(f"Requested Path: {path}")
```

Вебсайт будет показывать url, который мы вводили на сайте:

![[pathworks.png]]

Но так-же пользователь может вести код в строку:

![[inject.gif]]

И `alert` - это еще самое безобидное, что может сделать пользователь. 