---
title: Заметки
description: Описание заметок
---

{% for article in site.posts %}
  <h2>
    <a href="{{ article.url }}">{{ article.title }}</a>
  </h2>
{% endfor %}