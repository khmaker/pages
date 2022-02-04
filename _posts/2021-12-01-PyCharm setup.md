---
layout: default
title: PyCharm + autopep8 и flake8.
date: 2021-12-01
description: Руководство по настройке PyCharm для использования автоформаттера autopep8 и линтера flake8
tags: []
images_dir: "/pics/posts/PyCharm_setup/"
---
# Предисловие
Данное руководство написано с использованием Windows 10, для других ОС сочетания клавиш и некоторые настройки могут отличаться.

**Все скриншоты кликабельны.**

### Зачем всё это нужно
Данное руководство позволит вам настроить проверку синтаксиса при помощи flake8 и инструмент для приведения кода к стандарту [PEP 8](https://www.python.org/dev/peps/pep-0008/)
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
Поскольку линтером и автоформаттером пользоваться приходится практически в каждом проекте, 
мы установим всё необходимое в системный python.
Это позволит установить и настроить всё необходимое однажды и использовать в любом проекте.

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
            Создаем новый File Watcher
        </figcaption>
    </figure>
    <figure>
        <a href="{{ page.images_dir | relative_url }}{{ path }}2.png" target="_blank">
            <img src="{{ page.images_dir | relative_url }}{{ path }}2.png" alt=""/>
        </a>
        <figcaption>
            Заполняем нужные поля
        </figcaption>
    </figure>
</div>
<style>
    label, input {
        display: inline-block;
        width: 27.5%;
        text-align: left;
    }
    input {
        width: 70%;
    }
    .checkbox_label {
        width: 70%;
    }
    .checkbox_input {
        width: 5%;
    }
    .narrow {
        width: 23%;
    }
</style>
<form>
    New File Watcher
    <fieldset>
        <legend></legend>
        <label for="Name">Name: </label>
        <input type="text" name="Name" value="flake8" readonly disabled>
    </fieldset>
    <fieldset>
        <legend>Files to Watch</legend>
        <label for="File type">File type: </label>
        <input type="text" name="File type" value="Python" readonly disabled><br>
        <label for="Scope">Scope: </label>
        <input type="text" name="Scope" value="Project Files" readonly disabled><br>
    </fieldset>
    <fieldset>
        <legend>Tool to Run on Changes</legend>
        <label for="Program">Program: </label>
        <input type="text" name="Program" value="путь до flake8" readonly disabled><br>
        <label for="Arguments">Arguments: </label>
        <input type="text" name="Arguments" value="$FileDir$/$FileName$" readonly><br>
        <label for="Output paths to refresh">Output paths to refresh: </label>
        <input type="text" name="Output paths to refresh" value="" readonly disabled><br>
        <label for="Working directory">Working directory: </label>
        <input type="text" name="Working directory" value="$ProjectFileDir$" readonly><br>
        <label for="Environment variables">Environment variables: </label>
        <input type="text" name="Environment variables" value="" readonly disabled><br>
    </fieldset>
    <fieldset>
        <legend>Advanced Options</legend>
        <input class="checkbox_input" type="checkbox" name="Auto-save edited files to trigger the watcher" checked disabled>
        <label class="checkbox_label" for="Auto-save edited files to trigger the watcher">Auto-save edited files to trigger the watcher</label><br>

        <input class="checkbox_input" type="checkbox" name="Trigger the watcher on external changes" checked disabled>
        <label class="checkbox_label" for="Trigger the watcher on external changes">Trigger the watcher on external changes</label><br>

        <input class="checkbox_input" type="checkbox" name="Trigger the watcher regardless of syntax errors" disabled>
        <label class="checkbox_label" for="Trigger the watcher regardless of syntax errors">Trigger the watcher regardless of syntax errors</label><br>

        <input class="checkbox_input" type="checkbox" name="Create output file from stdout" disabled>
        <label class="checkbox_label" for="Create output file from stdout">Create output file from stdout</label><br>

        <label for="Show console">Show console: </label>
        <select disabled>
            <option value="Always" readonly>Always</option>
            <option value="On error" readonly>On error</option>
            <option value="Never" selected="selected" readonly>Never</option>
        </select>
        <br>
        <label for="Output filters">Output filters: </label>
        <input type="text" name="Output filters" value="$FILE_PATH$:$LINE$:$COLUMN$: $MESSAGE$" readonly><br>
    </fieldset>
</form>
<br>

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

### Создаём инструмент для использования автоформаттера
_Tools -> External Tools_ нажимаем на ➕
{% assign path = "External_tools/" %}
<figure>
    <a href="{{ page.images_dir | relative_url }}{{ path }}1.png" target="_blank">
        <img src="{{ page.images_dir | relative_url }}{{ path }}1.png" alt=""/>
    </a>
    <figcaption>
        Заполняем нужные поля
    </figcaption>
</figure>
<form>
    Edit Tool
    <fieldset>
        <legend></legend>
        <label for="Name">Name: </label>
        <input class="narrow" type="text" name="Name" value="flake8" readonly disabled>
        <label class="narrow" for="Group">Group: </label>
        <select class="narrow" disabled>
            <option value="External Tools" selected="selected" readonly>External Tools</option>
        </select>
        <label for="Description">Description: </label>
        <input type="text" name="Description" value="PEP 8 auto formatter" readonly disabled>
    </fieldset>
    <fieldset>
        <legend>Tool Settings</legend>
        <label for="Program">Program: </label>
        <input type="text" name="Program" value="путь до autopep8" readonly disabled><br>
        <label for="Arguments">Arguments: </label>
        <input type="text" name="Arguments" value="--in-place --aggressive --aggressive $FilePath$" readonly><br>
        <label for="Working directory">Working directory: </label>
        <input type="text" name="Working directory" value="$ProjectFileDir$" readonly><br>
    </fieldset>
    <fieldset>
        <legend>Advanced Options</legend>
        <input class="checkbox_input" type="checkbox" name="Synchronize files after execution" checked disabled>
        <label class="checkbox_label" for="ASynchronize files after execution">Synchronize files after execution</label><br>

        <input class="checkbox_input" type="checkbox" name="Open console for tool output" checked disabled>
        <label class="checkbox_label" for="Open console for tool output">Open console for tool output</label><br>

        <input style="margin-left: 5%;" class="checkbox_input" type="checkbox" name="Make console active on message in stdout" disabled>
        <label class="checkbox_label" for="Make console active on message in stdout">Make console active on message in stdout</label><br>

        <input style="margin-left: 5%;" class="checkbox_input" type="checkbox" name="Make console active on message in stderr" disabled>
        <label class="checkbox_label" for="Make console active on message in stderr">Make console active on message in stderr</label><br>


        <label for="Output filters">Output filters: </label>
        <input type="text" name="Output filters" value="$FILE_PATH$\:$LINE$\:$COLUMN$\:.*" readonly><br>
    </fieldset>
</form>
<br>

# Послесловие
### Как этим пользоваться
File watcher c flake8, если он активирован, на лету проверяет открытый файл и выводит замечания во вкладке _Problems_ `Alt+6`

Автоформаттер можно запустить из контекстного меню, либо назначить ему сочетание клавиш на ваш вкус.
<figure>
    <a href="{{ page.images_dir | relative_url }}{{ path }}2.png" target="_blank">
        <img src="{{ page.images_dir | relative_url }}{{ path }}2.png" alt=""/>
    </a>
    <figcaption>
        Вызываем автоформаттер из контекстного меню
    </figcaption>
</figure>