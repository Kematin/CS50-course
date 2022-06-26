# About lection

Ранее мы верстали страницу используя только `HTML`, из-за чего наши страницы получались <b>однообразные и простые,</b> 
однако используя второй язык `CSS` мы можем придать стиль нашему сайту. 
Добавить <b>цвета, расстояние, улучшить структуру и т.д.</b>

Есть несколько способов добавить CSS в наш сайт.<br>
Первый из них - использовать атрибут `style`
<pre>&lt;tag style="color:blue; align:53px; ..."&gt;Some text&lt;/tag&gt;</pre>

Так-же все теги внутри родительского тега с изменённым стилем будут измененны (DOM)
<br>В данном примере Some heading и Some text будут зелёного цвета
<pre>
&lt;div style="color:green"&gt;
    &lt;h2&gt;Some heading&lt;/h2&gt;
    &lt;p&gt;Some text&lt;/p&gt;
&lt;/div&gt;
</pre>

Второй способ изменить стиль - использовать тег `<style>` в родительском теге `<head>`
<br>В таком случае все теги обозначенные в style будут изменятся 
<pre>
&lt;head&gt;
    &lt;style&gt;
        h1 {
            color: red;
            text-align: center
        }
    &lt;/style&gt;
&lt;/head&gt;
.
.
&lt;h1&gt;Heading 1&lt;/h1&gt; <strong>Будет красного цвета в центре</strong>
&lt;h1&gt;Heading 2&lt;/h1&gt; <strong>Будет красного цвета в центре</strong>
</pre>

Чтобы использовать наш стиль на нескольких сайтах, можно его занести в отдельный файл
и уже внутри тега `<style>` указать его
> style.css
<pre>
span {
    color: lightblue;
    text-align: center;
}
</pre>
> style.html
<pre>
&lt;head&gt;
    &lt;link rel="stylesheet" href="style.html"
&lt;/head&gt;
</pre>

Стили определённых элементов можно привязывать по id
<pre>
&lt;head&gt;
    &lt;style&gt;
        #Text {
            color: red;
            font-family: Arial;
            text-align: center
        }
    &lt;/style&gt;
&lt;/head&gt;
.
.
&lt;p id="Text"&gt;Text 1&lt;/p&gt; <strong>Красный цвет, Arial по центру</strong>
&lt;p&gt;Text 2&lt;/p&gt; <strong>Обычный текст</strong>
</pre>
