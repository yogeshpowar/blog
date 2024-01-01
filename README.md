<a ref="/aboutMe"><img src="/blog/assets/images/yap.jpg" alt="LIFE"></a>
---
* [About Me](aboutMe)
---

# Blogs

Arranged in chronological Order. To view by tags click [here]({{ site.github.repository_url }}/tags)

<ul>
  {% for post in site.posts %}
    <li>
      {{ post.date | date: "%Y-%m-%d" }}: <a href="{{ site.github.repository_url }}{{ post.url }}">{{ post.title }}</a>
      <ul>
        {% if {{post.desc}} %}
            <li> <em>{{ post.desc }} </em> </li>
        {% endif %}
        <li> tags:
            {% for tag in {{post.tags}} %}
            <a href="tags#{{ tag }}">{{ tag }}</a>
            {% endfor %}
        </li>
      </ul>
    </li>
  {% endfor %}
</ul>

---

* Note: Most of these blogs were first published on Google's blogger have been ported
  to Github for my love towards
  [Markdown](https://daringfireball.net/projects/markdown/),
  [Git](https://git-scm.com/), [vimwiki](https://vimwiki.github.io/)

---
Except where otherwise noted, contents are licensed under a [Creative Commons
Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) International
license
----
