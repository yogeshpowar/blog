* [About Me](aboutMe)
---

# Blogs

- By Choronological Order

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ site.github.repository_url }}{{ post.url }}">{{ post.title }}</a>
      <ul>
        {% if {{post.desc}} %}
            <li> {{ post.desc }} </li>
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
