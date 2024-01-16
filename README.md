# Тестовое задание

<h3>1. Необходимо написать две функции:</h3>

<div>
1) функцию-архиватор, которая принимает на вход строку произвольной длины, 
а на выход выдает другую строку меньшей длины. <br>
Задача данной функции как можно сильнее сжать исходную строку. <br>
</div>
<div>
2) функцию-разархивирования, которая принимает на вход "сжатую" строку, 
а на выходе возвращает исходную строку без потерь.
</div>

<h3>2. Запрещено использовать специализированные библиотеки и методы.</h3>
<h3>3. Функция должны быть покрыта тестами. Тесты пишем в отдельном файле. 
Для тестов используем или unittest, или pytest.</h3>


# Реализация

<div>
На своё усмотрение решил использовать строки без использования цифр.
</div>
<div>
Алгоритм архивации заключается в поиске повторяющихся символов 
и превращении сегмента текста в символ и количество повторений. 
Например: <code>aaabbc -> a3b2c</code>.
</div>
<div>
Алгоритм разархивации обратен алгоритму архивации.
</div>
<div>
Добавлены блок тестирования в <code>tests.py</code>.
</div>