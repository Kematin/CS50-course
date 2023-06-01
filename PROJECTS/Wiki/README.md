# Wiki

*Project 1* - Design a Wikipedia-like online encyclopedia.

*All specification* - [URL](https://cs50.harvard.edu/web/2020/projects/1/wiki/#specification)

#### En
Functions of encyclopedia:
- Create new articale.
- Select random articale.
- Seacrh articale.
- Error page if articale is not exist.
- The list of all articles on the main page should be links to these same articles.
- If the request does not match any article, then the user is redirected to the article that matches this line.
    - for example: `ytho`-`Python`.
- On each article there should be a function - edit the article.
- After saving or completing a new article, the user is redirected to the main page.
- All changes to an article or the creation of a new page must occur in a `textarea` with `Markdown` markup.
- If the user has not used this markup, an error window is displayed.
- When editing a file, textarea must be pre-populated with Markdown content 


#### Ru
Функции онлайн энциклопедии:
- Создание новой статьи.
- Выборка случайной существующей статьи.
- Поиск статьи.
- Страница с ошибкой если статьи не существует.
- Список статьей на главной странице должны быть ссылками на эти самые страницы.
- Если при поиске не нашлось статьи то пользователя перенаправляет на статью
в названии которой есть данная подстрока.
    - Для примера: `ytho`-`Python`.
- На каждой страницы должна быть функция - редактировать статью.
- После сохранения или записи новой статьи пользователя перенаправляет на 
главную страницу.
- Все изменения статьи должны быть записаны в `textarea` с разметкой `Markdown`.
- Если данная разметка не используется пользователя перенаправляет на окно ошибки.
- При редактировании статьи textarea в заранее должно быть заполнено разметкой Markdown.
