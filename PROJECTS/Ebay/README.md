# Ebay Clone

Аукционный сайт электронной коммерции, подобный eBay,
который позволит пользователям публиковать списки аукционов, делать ставки на списки
, комментировать эти списки и добавлять списки в «список наблюдения».

Архитектура на miro - [url](https://miro.com/app/board/uXjVPxqe63o=/?share_link_id=699479903520)

## Start

1. Unzip commerce.zip
2. Go to commerce dir in terminal
3. Run `python manage.py makemigrations auctions`
4. Run `python manage.py migrate`
5. Start coding :D

## Routes

_Пользователь зарегистрирован_:
- Active listing
- Categories
- Watchlist
- Create listing
- Inactive listing
- Won listing
- Log out

_Пользователь не зарегистрирован_:
- Active listing
- Categories
- Inactive listing
- Login
- Register

## Technical Specification ([CS50](https://cs50.harvard.edu/web/2020/projects/2/commerce/))

- __Модели__.
<br>Должно быть минимум 4 модели в базе данных, характеризиующие:
    - Пользователя
    - Аукционные списки
    - Каждый отдельный предмета продаж
    - Комментарии.
- __Cоздание Объявления__.
<br>Каждый пользователь может создать объявление на главной странице.
Объявление состоит из следующих элементов:
    - Заголовок
    - Текстовое описание
    - Начальная ставка
    - Ссылка на изображение предмета (если ее нет, она заменяется дефолтной)
- __Страница Объявления__.
<br>Перейдя по объявлению пользователь должен видеть всю информацию
о нем, включая текущую цену. _Если пользователь зарегестрирован_:
    - Он может добавить текующее объявление в `"Корзину"`, если предмет уже там, 
    то он может удалить его из корзины.
    - Он может делать ставку больше минимальной и предыдущей ставки (если такая имеется),
    иначе выдается ошибка.
    - Если он создатель объявления тогда он может его `закрыть`. Тогда победитель 
    аукциона (человек с большей ставкой) забирает данный предмет и объявление 
    переходит в `неактивное`.
    - Если он победитель аукциона, ему должно быть отображенно это. Объявление переходит
    в `выйгранное`.
    - Он может добавлять комментарии к объявлению. Так-же отображаются все остальные комментарии.
- __Корзина__.
<br>У зарегестрированного пользователя должны быть корзина, в которой отображаются 
все объявления добавленные в нее, а так-же нажав на любое из них идет переход
на данное объявление
- __Категории__.
<br>Страница на которой отображаются все категории объявлений, нажав на любое из 
них, пользователю отображаются все объявления данной категории.
- __Django Admin Interface__.
<br>Через интерфейс админа можно просматривать, добавлять, редактировать и удалять:
    - Объявления (и их содержимое)
    - Комментарии
    - Ставки

## Technical Specification (Addition)

- __Неактиваное__.
<br> Страница на которой отображаются `закрытые` объявления, нажав на которые
можно увидеть полное его описание, победителя и его ставку.
- __Выйгранное__.
<br> Страница у зарегестрированного пользователя, на которой отображаются все 
выйгранные объявления данного пользователя.
