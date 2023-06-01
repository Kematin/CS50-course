Все css селекторы можно посмотреть перейдя по данной ссылке > <strong><a href="https://www.w3schools.com/cssref/css_selectors.asp">ТЫК</a></strong>
<br>Наиболее важные я укажу в таблице
<table>
    <thead>
        <tr>
            <th>Селектор</th>
            <th>Пример</th>
            <th>Описание</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>a, b</td>
            <td>h3, h2</td>
            <td>Все элементы h3 и h2 изменяются</td>
        </tr>
        <tr>
            <td>a b</td>
            <td>div p</td>
            <td>Все элементы p внутри элемента div изменяются</td>
        </tr>
        <tr>
            <td>a > b</td>
            <td>div > p</td>
            <td>Все элементы p с родительским тегом div изменяются</td>
        </tr>
        <tr>
            <td>a + b</td>
            <td>div + p</td>
            <td>Изменяется первый элемент p сразу после элемента div</td>
        </tr>
        <tr>
            <td>a[b=c]</td>
            <td>a[href="some href"]</td>
            <td>Изменяются все элементы a атрибут href которых равен "some href"</td>
        </tr>
        <tr>
            <td>a:b</td>
            <td>button:hover</td>
            <td>Изменяется подкласс элемента button - hover</td>
        </tr>
    </tbody>
</table>
