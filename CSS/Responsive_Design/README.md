<h2 style="text-align: center">Части Responsive Design</h2>
<ul>
    <li><strong>Viewport</strong></li>
    <li><strong>Media Queries</strong></li>
    <li><strong>Flexbox</strong></li>
    <li><strong>Grids</strong></li>
</ul>
<h3 style="text-align: center">Viewport</h3>
<strong>Viewport</strong> - это видимая область элементов на сайте пользователю несмотря с какого устройства
он зашел. Если не настраивать эту область для разных устройств, то многие важные элементы на разных устройствах
могут сжиматься, уменьшаться или вовсе пропадать как на примере снизу.

![Bad viewport](viewport.png)

Нужный результат.

![Good viewport](phone.png)

Что-бы наша веб страница на другом устройстве выглядела чуточку лучше можно добавить
данную строчку в наш html файл.
<pre>
&lt;head&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"
&lt;/head&gt;
</pre>
<h3 style="text-align: center">Media Queries</h3>
<strong>Медиа запросы</strong> - это функция css позволяющия браузеру различных устройств
рендерить контент адаптируясь к различным условиям, например разрешение экрана.
<br>Так это будет выглядеть в коде.
<pre>
&lt;head&gt;
    &lt;style&gt;
        @media (min-width: 600px) {
            body {
                backround-color: red
            }
        }
    &lt;/style&gt;
&lt;/head&gt;
</pre>

> @media - объявляет о медиа запросе

> (min-width: 600px) - задает условие если разрешение экрана 600 или более пикселей

> body {} - изменяет тело веб сайта

Мы так-же можем добавлять больше медиа запросов и условий для них, изменяя не только цвет сайта,
но и например размер определённого div

<h3 style="text-align: center">Flexbox</h3>
<strong>Flexbox</strong> - представляет собой модель веб-макета CSS 3. Это способ компановки элементов
в зависимости от разрешения экрана.
<pre>
&lt;head&gt;
    &lt;style&gt;
        #container {
            display: flex;
            flex-wrap: wrap;
        }
    &lt;/style&gt;
&lt;/head&gt;
</pre>

> display: flex - объявляем flexbox для элемента

> flex-wrap: wrap - метод компановки (перенос элемента на следующую строку)

<h3 style="text-align: center">Grid</h3>
<strong>Grid layout</strong> - функция CSS 3, позволяющая с легкостью создавать макеты сеток
на веб странице.
<pre>
&lt;head&gt;
    &lt;style&gt;
        #grid {
            display: grid;
            grid-column-grap: 30px;
            grid-row-grap: 15px;
            grid-template-columns: 300px 120px 800px auto;
        }
    &lt;/style&gt;
&lt;/head&gt;
</pre>

> display: grid - объявляем grid компановку

> grid-column-grap: 30px - расстояние между столбцами

> grid-row-grap: 15px - расстояние между строками

> grid-template-columns: ... - сколько будет столбцов в строчке и их размеры (4 шт в данном примере)
