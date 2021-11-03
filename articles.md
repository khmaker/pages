---
title: Заметки
description: Описание заметок
---

<p>{{ site.permalinks }}</p>
{% for article in site.articles %}
  <h2>
    <a href="{{ article.url }}">{{ article.title }}</a>
  </h2>
{% endfor %}