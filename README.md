<a href="aboutMe"><img class="profile-photo" src="assets/images/yap.jpg" alt="LIFE"></a>

* [About Me](aboutMe)

# Blogs

Arranged in chronological order. To view by tags click [here]({{ site.github.repository_url }}/tags)

<ul class="post-list">
  {% for post in site.posts %}
    <li>
      <a class="post-list-title" href="{{ site.github.repository_url }}{{ post.url }}">{{ post.title }}</a>
      <div class="post-list-meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time>
        {% for tag in post.tags %}
          <a class="tag" href="tags#{{ tag }}">{{ tag }}</a>
        {% endfor %}
      </div>
      {% if post.desc %}
        <div class="post-list-desc">{{ post.desc }}</div>
      {% endif %}
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
