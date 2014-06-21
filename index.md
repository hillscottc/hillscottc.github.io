---
layout: page
markdown: redcarpet
title: Study
tagline: Data structures and algorithms.
---
{% include JB/setup %}

    

### Programming

<ul>
  {% assign pages_list = site.pages %}
  {% assign group = 'programming' %}
  {% include JB/pages_list %}
</ul>

### Data Structures

<ul>
  {% assign pages_list = site.pages %}
  {% assign group = 'data_structs' %}
  {% include JB/pages_list %}
</ul>

### Problems

<ul>
  {% assign pages_list = site.pages %}
  {% assign group = 'problems' %}
  {% include JB/pages_list %}
</ul>


### Code to know

<ul>
  {% assign pages_list = site.pages %}
  {% assign group = 'code' %}
  {% include JB/pages_list %}
</ul>

### Python Code
  
  - [index](/pycode/)


[Misc](misc.html)

## Posts

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>



#### Sources

- Harrington at Loyola, Comp 363, Algorithms [source](http://anh.cs.luc.edu/363/notes/)
- InteractivePython, Problem Solving with Algorithms and Data Structures [source](http://interactivepython.org/courselib/static/pythonds/index.html)
- Vazirani at Berekely, Algorithms [source](http://www.cs.berkeley.edu/~vazirani/algorithms/)





