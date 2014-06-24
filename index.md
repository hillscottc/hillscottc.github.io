---
layout: page
markdown: redcarpet
title: Study
tagline: Data structures and algorithms.
---
{% include JB/setup %}

[Misc](pages/misc.html)

### Posts

Posts [by Tag](tags.html)

Posts [by Category](categories.html)

All Posts:  
{% for post in site.posts %}
- [{{ post.title }}]({{ BASE_PATH }}{{ post.url }})
{% endfor %}


### Code to know

<ul>
{% assign pages_list = site.pages %}
{% assign group = 'code' %}
{% include JB/pages_list %}
</ul>


#### Sources

- Harrington at Loyola, Comp 363, Algorithms [source](http://anh.cs.luc.edu/363/notes/)
- InteractivePython, Problem Solving with Algorithms and Data Structures [source](http://interactivepython.org/courselib/static/pythonds/index.html)
- Vazirani at Berekely, Algorithms [source](http://www.cs.berkeley.edu/~vazirani/algorithms/)





