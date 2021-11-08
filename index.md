---
title: Заголовок главной страницы
description: Описание содержимого главной страницы
---
{% if site.posts %}
<h1>posts</h1>
    <ul>
        {% for post in site.posts %}
            <li><a href="{{ site.url }}{{ post.url }}">{{ post.title }}</a></li>
        {% endfor %}
    </ul>
{% endif %}

{% if site.tags %}
<h1>tags</h1>
    {% for tag in site.tags %}
      <h3>{{ tag[0] }}</h3>
      <ul>
        {% for post in tag[1] %}
          <li><a href="{{ post.url }}">{{ post.title }}</a></li>
        {% endfor %}
      </ul>
    {% endfor %}
{% endif %}
