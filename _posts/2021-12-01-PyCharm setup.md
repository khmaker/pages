---
layout: default
title: PyCharm и все, все, все.
date: 2021-12-01
description: Руководство по настройке PyCharm для использования автоформаттера autopep8 и линтера flake8
tags: [PyCharm]
images_dir: "/pics/posts/PyCharm_setup/"
---
# Предисловие
Данное руководство написано с использованием Windows 10, для других ОС сочетания клавиш и некоторые настройки могут отличаться.

**Все скриншоты кликабельны.**

### Необходимые условия
Должны быть установлены:
* [Python](https://www.python.org/downloads/)
* [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download/)
* [Git](https://git-scm.com/download/win)

### ПО использованное в данном руководстве
* Python 3.7.0
* PyCharm 2021.2.3 (Community Edition)
* Git version 2.34.1.windows.1


# Руководство
### Открываем настройки
При первом запуске PyCharm мы можем найти ссылку _All settings…_ на вкладке _Customize_.
При работе над проектом настройки можно найти в меню _File_, либо открыть по нажатию `Ctrl+Alt+S`
<figure>
    <a href="{{ page.images_dir | relative_url }}settings.png" target="_blank">
        <img src="{{ page.images_dir | relative_url }}settings.png" alt="Вкладка Customize"/>
    </a>
    <figcaption>
        Вкладка Customize
    </figcaption>
</figure>

### Меняем терминал
<small>* данное действие опционально</small>

Если, по какой-то причине вас не устраивает стандартный терминал вашей ОС, то его всегда можно заменить в настройках. 

_Tools -> Terminal_ в разделе Application Settings в поле Shell path можно указать путь до нужного вам терминала.
<figure>
    {% assign path = "Terminal/" %}
    <a href="{{ page.images_dir | relative_url }}{{ path }}1.png" target="_blank">
        <img src="{{ page.images_dir | relative_url }}{{ path }}1.png" alt="Вкладка Customize"/>
    </a>
    <figcaption>
        
        Меняем стандартный терминал на Git bash
    </figcaption>
</figure>

### Устанавливаем необходимые зависимости
    # TODO: добавить причину установки в системный python

* [flake8](https://github.com/pycqa/flake8)
* [flake8-broken-line](https://github.com/wemake-services/flake8-broken-line)
* [autopep8](https://github.com/hhatto/autopep8)

<div class="fig_wrap">
    {% assign path = "Python_Interpreter/" %}
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}1.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}1.png" alt=""/>
        </a>
        <figcaption>
            Python Interpreter
        </figcaption>
    </figure>
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}2.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}2.png" alt=""/>
        </a>
        <figcaption>
            Добавляем новый интерпретатор
        </figcaption>
    </figure>
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}3.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}3.png" alt=""/>
        </a>
        <figcaption>
            Выбираем System Interpreter и указываем путь до установленного python
        </figcaption>
    </figure>
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}4.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}4.png" alt=""/>
        </a>
        <figcaption>
            зависимости установленные в выбранном интерпретаторе
        </figcaption>
    </figure>
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}5.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}5.png" alt=""/>
        </a>
        <figcaption>
            flake8
        </figcaption>
    </figure>
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}6.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}6.png" alt=""/>
        </a>
        <figcaption>
            flake8-broken-line
        </figcaption>
    </figure>
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}7.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}7.png" alt=""/>
        </a>
        <figcaption>
            autopep8
        </figcaption>
    </figure>
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}8.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}8.png" alt=""/>
        </a>
        <figcaption>
            После устновки нужных зависимостей
        </figcaption>
    </figure>
</div>

### Устанавливаем необходимый плагин
Переходим в _Plugins_, в поисковой строке набираем _File Watchers_ и нажимаем _Install_
Чтобы плагин отобразился в меню нужно перезапустить PyCharm.
{% assign path = "File_Watchers/" %}
<figure>
    <a href="{{ page.images_dir | relative_url }}{{ path }}0.png" target="_blank">
        <img src="{{ page.images_dir | relative_url }}{{ path }}0.png" alt=""/>
    </a>
    <figcaption>
        Необходимый плагин установлен
    </figcaption>
</figure>

### Создаем File watcher с flake8
_Tools -> File Watchers_ нажимаем на ➕ и выбираем _\<custom\>_
<div class="fig_wrap">
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}1.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}1.png" alt=""/>
        </a>
        <figcaption>
            1
        </figcaption>
    </figure>
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}2.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}2.png" alt=""/>
        </a>
        <figcaption>
            2
        </figcaption>
    </figure>
</div>
    #TODO: Текстовые данные полей 
<div class="fig_wrap">
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}3.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}3.png" alt=""/>
        </a>
        <figcaption>
            File watcher создан, но не активирован
        </figcaption>
    </figure>
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}4.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}4.png" alt=""/>
        </a>
        <figcaption>
            File watcher активирован
        </figcaption>
    </figure>
</div>


    #TODO: Дописать про автоформаттер
