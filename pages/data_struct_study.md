---
layout: page
title: Data Structures and Algorithms
tagline: study material
---
{% include JB/setup %}

### Posts

- Grouped by [Tag](/tags.html), or by [Category](/categories.html)

- All Posts:  
  | {% for post in site.posts %} [{{ post.title }}]({{ BASE_PATH }}{{ post.url }}) |{% endfor %}

### Code Samples

<ul>
{% assign pages_list = site.pages %}
{% assign group = 'code' %}
{% include JB/pages_list %}
</ul>


### Sources
- [TopCoder](http://community.topcoder.com/)
- [Harrington at Loyola, Comp 363, Algorithms](http://anh.cs.luc.edu/363/notes/)
- [InteractivePython, Problem Solving with Algorithms and Data Structures](http://interactivepython.org/courselib/static/pythonds/index.html)
- [Vazirani at Berekely, Algorithms](http://www.cs.berkeley.edu/~vazirani/algorithms/)





