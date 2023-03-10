- [User Interfaces](#UserInterfaces)
- [Single Page Application](#SPA)

# UserInterfaces

Интерфейс пользователя - это то как пользователь взаимодействует с веб сервером.
Задача разработчиков сделать взаимодействие как можно приятней и удобней для пользователя

# SPA

При создание веб сайтов, часто приходится добавлять дополнительные страницы в него. Если
же сайт небольшой то можно вместо перегрузки сайта джангой просто манипулировать DOM
элементами, тем самым иллюзиорно добавляя дополнительные страницы.

Пример в файле [SPA.js](SPA.js) и [SPA.html](SPA.html)

Так-же с помощью связки django + js можно удобно манипулировать данными. Чтобы не перегружать
страницу данными, можно их загружать только при определенном запросе.

Пример в проекте [spa](spa)

Более детальное объяснение:

**index.html**

Имеется 3 кнопки для переключения секций и основной div в котором будет
помещенны данные о секции.

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Single Page</title>
        <style>
        </style>
        <script src="{% static 'index.js' %}"></script>
    </head>
    <body>
        <h1>Hello!</h1>
        <button data-section="1">Section 1</button>
        <button data-section="2">Section 2</button>
        <button data-section="3">Section 3</button>
        <div id="content">
        </div>
    </body>
</html>
```

**views.py**

На сервере есть путь _section/<int: num>_. При GET (HttpRequest), запросе на этот путь,
отдается ответ (response, HttpResponse) в виде одного из текстов массива texts по индексу _num-1_.

```python
texts = [text_1, text_2, text_3]
def section(request, num: int):
    if num in range(1, 4):
        return HttpResponse(texts[num-1])
    else:
        return Http404
```

**index.js**

При нажатие на кнопку одна из секций становится отображаемой. Так-же идет
GET запрос на страницу сервера, по пути _section/pageNum_, а из ответа забирается
один из текстов сервера, который будет отображен на странице.

Так-же применяется метод history, который создает _историю посещений_, и при нажатии
на стрелку прошлой страницы, будет открыта ранее отображаемая секция 
(_это контроллирует функция метода window **onpopstate**_). 

```js
// When back arrow is clicked, show previous section
window.onpopstate = function(event) {
    showSection(event.state.section);
}

function showSection(section) {
    // Get text from server by GET request
    fetch(`/section/${section}`)
    .then(response => response.text())
    .then(text => {
        console.log(text);
        document.querySelector('#content').innerHTML = text;
    });

}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            const section = this.dataset.section;

            // Add the current state to the history
            history.pushState({section: section}, "", `section${section}`);
            showSection(section);
        };
    });
});
```
