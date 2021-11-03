---
title: Заметки
description: Описание заметок
---

<p>{{ site }}</p>
<p>{{ site.articles }}</p>
{% for article in site.articles %}
  <a href="{{ article.url }}">
    <h2>{{ article.title }}</h2>
  </a>
{% endfor %}Test