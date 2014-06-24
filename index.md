---
layout: page
markdown: redcarpet
title: Study
tagline: Data structures and algorithms.
---
{% include JB/setup %}


[Misc](pages/misc.html)


### Posts

{% for post in site.posts %}
  - [{{ post.title }}]({{ BASE_PATH }}{{ post.url }})
{% endfor %}

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


### Code

- [/code/](/code/)
- Code to know

  <ul>
    {% assign pages_list = site.pages %}
    {% assign group = 'code' %}
    {% include JB/pages_list %}
  </ul>


#### Sources

- Harrington at Loyola, Comp 363, Algorithms [source](http://anh.cs.luc.edu/363/notes/)
- InteractivePython, Problem Solving with Algorithms and Data Structures [source](http://interactivepython.org/courselib/static/pythonds/index.html)
- Vazirani at Berekely, Algorithms [source](http://www.cs.berkeley.edu/~vazirani/algorithms/)





