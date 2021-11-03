---
title: Заметки
description: Описание заметок
---

{% for article in site.articles %}
  <a href="{{ article.url }}">
    <h2>{{ article.title }}</h2>
  </a>
{% endfor %}