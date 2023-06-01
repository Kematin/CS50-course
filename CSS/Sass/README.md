<h2>SASS</h2>
<strong>Sass</strong> - это мета язык на основе CSS который имеет больший функционал.
Например поддерживает переменные, что упрощает написание кода.

Файлы Sass имеют разрешение `.scss`

> variables.scss

<pre>
$color: lightpink;

ul {
    font-size: 14px;
    color: $color;
}

ol {
    font-size: 18px;
    color: $color;
}
</pre>

> $color - объявление переменной
> <br>ul/ol{color: $color} - использование переменной

Проблема в том что браузер не может считывать файлы с разрешением scss,
поэтому чтобы указать наш стиль в `<link>` придётся его компилировать
в css файл командой и уже css файл импортировать в наш html файл

> sudo apt install sass
<pre>sass filename.scss:filename.css</pre>

Но в таком случае для изменения стился придётся каждый раз перекомпелировать наш 
scss файл, что очень неудобно. 

Для автоматизации процесса надо ввести команду: 
<pre>sass --watch filename.scss:filename.css</pre>

> *Команда не асинхронная и мы не сможем пользоваться окном терминала пока не прекратим процесс.*

Так-же sass имеет более лёгкий синтакс что показано в файле `nesting.scss`.

<h3>Наследование</h3>
Данный язык имеет наследование в коде.

<pre>
%text {
    color: blue;
    padding: 20px;
    margin: 20px;
    text-align: center;
}

#element-1 {
    @extend %text;
    background-color: blue;
}

#element-2 {
    @extend %text;
    background-color: red;
}
</pre>

> %text {...} - создание стиля для наследования
> <br>@extend %text - наследование стиля
