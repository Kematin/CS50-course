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

Имеется 3 условные страницы (секции), которые выключены функцией disablePages.

```html
<main>
	<button data-page="1">Page 1</button>
	<button data-page="2">Page 2</button>
	<button data-page="3">Page 3</button>

	<div id="page1" class="pages">
		<h2>This is page 1</h2>
		<p id="text1"></p>
	</div>
	<div id="page2" class="pages">
		<h2>This is page 2</h2>
		<p id="text2"></p>
	</div>
	<div id="page3" class="pages">
		<h2>This is page 3</h2>
		<p id="text3"></p>
	</div>
</main>
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

```js
function disablePages() {
	pages = document.querySelectorAll(".pages");
	pages.forEach((page) => {
		page.style.display = "none";
	});
}

function showPage(pageNum) {
	disablePages();

	activePage = document.querySelector(`#page${pageNum}`);
	activePage.style.display = "block";

	fetch(`/section/${pageNum}`)
		.then((response) => response.text())
		.then((text) => {
			newP = document.querySelector(`#text${pageNum}`);
			newP.innerHTML = text;
			activePage.append(newP);
		});
}
```
