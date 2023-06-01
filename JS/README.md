 - [JavaScript](#JavaScript)
 - [Events](#Events)
 - [Variables](#Variables)
 - [querySelector](#querySelector)
 - [DOM Manipulation](#DOM)
    - [JS Console](#Console)
    - [Arrow functions](#ArrowFunctions)
    - [TODO list](#TODO)
 - [Intervals](#Intervals)
 - [Local Storage](#LocalStorage)
 - [APIs](#APIs)
    - [JavaScript Objects](#Objects)
    - [Currency Exchange](#CurrencyExchange)


# JavaScript

Как мы знаем клиент "общается" с сервером через http запрос/ответ. Django является
серверной частью разработки, а javascript в свою очередь запускает скрипты на клиентской
части, без запросов, обрабатывая напрямую html шаблон.

**Пример добавления джаваскрипта в html в файле [HelloWorld.html](HelloWorld.html)**


# Events

JS поддерживает event-driven программирование, т.е. обрабатывает такие действия клиента
как нажатие на кнопку, движение курсора и т.д.

**Пример использования в файле [Event.html](Event.html)** в котором функция обрабатывает 
действия клиента - нажатие на кнопку и выдает окно с информацией.


# Variables

Виды переменных:
- var: глобальная переменная
- let: локальная переменная для определенных блоков или функций
- const: неменяющееся перменная 

**Пример использования в файле [Variables.html](Variables.html)**


# querySelector

querySelector функция из модуля document которая помогает манипулировать 
DOM элементами (добавлять, удалять, изменять, читать)

**Пример использования в файле [Query.html](Query.html)**

Так-же там есть строчка ``if (header.innerHTML === "Hello!")``. Тройной знак равно 
означает что переменная проверяется не только по значению, но и по типу.


# DOM 

**Пример DOM манипуляции [DOM.html](DOM.html) и [DOM.js](DOM.js)**. 

В данном файле есть строчка:
``alert(`Count is now ${counter}`)``. Благодаря синтаксису в котором строчка пишется
в особых кавычках, можно отображать переменную counter.

Так-же в html файле лушче не внедрять напрямую js или css, поэтому можно заменить
аттрибут в теге button на ``document.querySelector('button').onclick = count;``,
тогда аттрибут заменяется не напримую а через скрипт. Но js код рендерится быстрее 
чем кнопка, так что просто данную строчку в скрипт вписать нельзя.

Решения проблемы:
```js
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('button').onclick = count;
});
```

1. Вызывается функция addEventListener которая берет 2 аргумента:
    1. Какое либо действие (будь то нажатие на кнопку или загрузка страницы)
    2. Функция которая будет запускаться при событие
2. Аттрибут кнопки изменяктся только если загружается страница, вызывая анонимную функцию

Способ как перенести код в отдельный файл так-же как и в css.


**Еще один пример DOM манипуляции в файле [Colors.html](Colors.html) и [Colors.js](Colors.js)**


## Console

Консоль джаваскрипта отличная вещь для тестинга и деббагинга небольших фич. Пример 
использования так-же в [Colors.js](Colors.js)


## ArrowFunctions

Как я понял просто упращает написание ``function func(arg) {}``, на ``func = (arg) => {}``. 
Но зачем? :o. Подобным синтаксисом мы передаем в переменную функцию, а при дефолтном написание 
просто ее инициализируем в памяти. 


## TODO

Пример реализации с комментариями в файле [Todo.js](todo.js) и [Todo.html](todo.html)


# Intervals

Интервалы js вызываются командой ``setInterval(func, tickTime);`` и позволяют повторять 
каждую tickTime милисикунду функцию func.

Пример реализации в файле [Interval.js](Interval.js) и [Interval.html](Interval.html)


# LocalStorage

Во время обновления страницы сбрасываются все наши изменения в ходе логики: цвет текста, счетчик и т.д.
Это можно исправить благодаря **локальному хранилищу браузера пользователся**, в котором можно сохранять информацию
для будущего использования. Информация локального хранилища сохраняется в виде **ключ-значение**. Основные функции
локального хранилища:

```js
// Get value from local storage with this key
localStorage.getItem(key)

// Set value into local storage with this key
localStorage.setItem(key, value)
```

Пример реализации в файле [Storage.js](Storage.js) и [Storage.html](Storage.html)

# APIs

## Objects

**JavaScript Object** - объект, схожий по синтаксису на словарь питона, в котором хранятся данные
в виде ключ-значение. Объекты js полезны тем, что с помощью них удобно передавать данные, тем более 
при использование апишек. Обычно данные от апишек возвращаются в виде **JSON** (JS Object Notation).

Пример объекта:
```js
var person = {
    name: "Jhon",
    age: 50
}
// Jhon (also person["name"] will output same result)
console.log(person.name)

person.age = 25

// 25
console.log(person.age)
```

Пример работы с объектом джаваскрипта в файле [Objects.js](Objects.js) и [Objects.html](Objects.html)


## CurrencyExchange

Пример использования API в файле [Currency.js](Currency.js) и [Currency.html](Currency.html).

В данном проекте используется API [European Central Bank’s Exchange Rate API](https://exchangeratesapi.io/).
Для создания API запросов используется AJAX (Asynchronous JavaScript And XML), который позволяет 
брать данные с других страних, даже когда наша уже загруженна. 

Синтаксис API запросов:
```js
function callAPI() {
    // Some request url api
    url = "https://api.exchangeratesapi.io/latest?base=USD"

    // Send get request to the url
    fetch(url)
    
    // Put response in json format
    .then(response => response.json())

    // Get our data with json format and put its into another func
    .then(data => changeData(data))
}
```

Пример работы с комментариями в файле [Currency.js](Currency.js) и [Currency.html](Currency.html)
