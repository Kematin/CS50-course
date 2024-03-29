- [User Interfaces](#UserInterfaces)
- [Single Page Application](#SPA)
- [Scroll](#Scroll)
  - [Infinity Scroll](#InfinityScroll)
- [Animation](#Animation)
- [React](#React)
  - [Game: "Addition"](#Addition)

# UserInterfaces

Интерфейс пользователя - это то как пользователь взаимодействует с веб сервером.
Задача разработчиков сделать взаимодействие как можно приятней и удобней для пользователя

# SPA

При создание веб сайтов, часто приходится добавлять дополнительные страницы в него. Если
же сайт небольшой то можно вместо перегрузки сайта джангой просто манипулировать DOM
элементами, тем самым иллюзиорно добавляя дополнительные страницы.

**Пример в файле [SPA.js](SPA.js) и [SPA.html](SPA.html)**

Так-же с помощью связки django + js можно удобно манипулировать данными. Чтобы не перегружать
страницу данными, можно их загружать только при определенном запросе.

**Пример в проекте [spa](spa).**

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
		<style></style>
		<script src="{% static 'index.js' %}"></script>
	</head>
	<body>
		<h1>Hello!</h1>
		<button data-section="1">Section 1</button>
		<button data-section="2">Section 2</button>
		<button data-section="3">Section 3</button>
		<div id="content"></div>
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

Так-же применяется объек history с методом **_pushState({name: value}, "", route)_**,
который создает _историю посещений_, и при нажатии
на стрелку прошлой страницы, будет открыта ранее отображаемая секция
(_это контроллирует метод объекта window **onpopstate**_).

```js
// When back arrow is clicked, show previous section
window.onpopstate = function (event) {
	showSection(event.state.section);
};

function showSection(section) {
	// Get text from server by GET request
	fetch(`/section/${section}`)
		.then((response) => response.text())
		.then((text) => {
			console.log(text);
			document.querySelector("#content").innerHTML = text;
		});
}

document.addEventListener("DOMContentLoaded", function () {
	document.querySelectorAll("button").forEach((button) => {
		button.onclick = function () {
			const section = this.dataset.section;

			// Add the current state to the history
			history.pushState({ section: section }, "", `section${section}`);
			showSection(section);
		};
	});
});
```

# Scroll

При создание секций использовался объект **_window_**, с помощью которого
можно управлять основным окном пользователя. Несколько интересных параметров:

```
window.innerWidth: длинна окна в пикселях
window.innerHeight: высота окна в пикселях
```

Несмотря на это, сам по себе документ может быть больше самого окна, поэтому мы можем
скроллить страницы и для работы с этим так-же есть отдельные параметры:

```
window.scrollY: сколько пользователь пролистал вниз в пикселях
document.body.offsetHeight: высота документа в пикселях
```

![IMG](https://cs50.harvard.edu/web/2020/notes/6/images/scroll.png)

Благодаря этому, например, можно контроллировать достиг ли пользователь конца страницы,
выражением `window.scrollY + window.innerHeight >= document.body.offsetHeight`.

**Пример в файле [Scroll.js](Scroll.js) и [Scroll.html](Scroll.html)**

## InfinityScroll

Прошлая работа с окном полезна при создание страницы с бесконечным скроллингом вниз.
Т.е. при заходе на сайт пользователю загружаются 10 постов и при каждом скроллинге до конца страницы,
загружаются еще 10 постов и т.д.

**Реализация бесконечного скроллинга страницы в проекте [infinity](infinity)**

**views.py**

Создается отдельный путь на сайте: /posts. При get запросе на него отдается в ответ
данные о постах в json формате.

```python
def posts(request):
    # Get start point and end point
    start = int(request.GET.get("start") or 1)
    end = int(request.GET.get("end") or (start+9))

    # Get array of posts
    data = [f"Post #{i}" for i in range(start, end+1)]
    time.sleep(1)

    '''
    route ./posts?start=5 will return:
    {
        Posts: [
                "Post 5",
                "Post 6",
                ...,
                "Post 15"
            ]
    }
    route ./posts?start=5&end=6 will return:
        {Posts: ["Post 5", "Post 6"]}
    '''
    return JsonResponse({
        "posts": data
    })
```

**index.js**

Файл js создает get запросы на сервер по пути /posts с атрибутами start и end, для получения
информации о постах. Каждый раз когда пользователь доходит до конца страницы, создается get запрос
и отображается новая информация по постам на странице.

```js
let counter = 1;

// How many posts will be get from server
const quantity = 15;

// Setup function on scroll
window.onscroll = checkBottomPage;
document.addEventListener("DOMContentLoaded", load);

function checkBottomPage() {
	if (window.scrollY + window.innerHeight >= document.body.offsetHeight) {
		load();
	}
}

function load() {
	start = counter;
	end = start + quantity - 1;
	counter = end + 1;

	// Get data from server and put in json
	fetch(`/posts?start=${start}&end=${end}`)
		.then((response) => response.json())
		.then((data) => {
			// in forEach loop create posts
			data.posts.forEach(createPost);
		});
}

function createPost(content) {
	const newPost = document.createElement("div");
	newPost.className = "post";
	newPost.innerHTML = content;

	document.querySelector("#posts").append(newPost);
}
```

# Animation

Так-же с помощью css можно создавать анимации, а благодаря js управлять ими.
В фукнциях анимации мы показываем как изменяется элемент,
с помощью конструкции `from {} to {}` или `0% {} 20% {} n% {} 100% {}`.
И создаются такие функции с помощью `@keyframes`

Пример конструкции анимации:

```css
@keyframes hello {
	from {
		font-size: 10px;
	}
	to {
		font-size: 50px;
	}
}

#hello {
	animation-name: hello;
	animation-duration: 3s;
	animation-iteration-count: 2;
	animation-fill-mode: forwards;
}
```

**Пример манипуляции анимацией в файле [Animation.js](Animation.js) и [Animation.css](Animation.css)**

**Еще один пример в проекте [infinity](infinity)**

# React

React - фреймворк библиотека джаваскрипта. До этого, используя чистый джаваскрипт,
программирование считалось императивным. React в свою очередь использует декларативный
метод, что позволяет не беспокоится о том _как_ отображается элемент.

_Императивный метод:_

```
View:
<h1>0</h1>

Logic:
let num = parseInt(document.querySelector("h1").innerHTML);
num += 1;
document.querySelector("h1").innerHTML = num;
```

_Декларативный метод:_

```
View:
<h1>{num}</h1>

Logic:
num += 1;
```

React построен на идеи использования компонентов и их взаимодействий.

> Фреймворк React построен на идее компонентов, каждый из которых может иметь базовое состояние. Компонент - это то, что вы видите на веб-странице, например, пост или панель навигации, а состояние - это набор переменных, связанных с этим компонентом. Прелесть React в том, что при изменении состояния React автоматически изменяет DOM соответствующим образом.

Есть множество способов использовать реакт  
(в том числе команда [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html)).
В данном примере будет использоватся напрямую в html.
Для этого надо импортировать 3 библиотеки:

1. React (Определяет компоненты и их поведение)
2. ReacDOM (Внедряет React компоненты в html)
3. Babel (Компилирует jsx реакта в чистый js код)

**Структура компонентов React:**

```js
<div id="app"></div>
<script type="text/babel">
    // Create main component App
    function App() {
        // Use another components in App
        // Also we can setup props for compontent (name="Jhon")
        return (
            <div>
                <h1>Welcome!</h1>
                <Hello name="Jhon" />
            </div>
        );
    }

    // Render main component to DOM elements in div with id app
    ReactDOM.render(<App />, document.querySelector("#app"));
</script>
```

**Пример работы с React в [React.html](React.html)**

## Addition

**Пример реализации игры в решение примеров в файле [Addition.html](Addition.html)**
