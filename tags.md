* [About Me](aboutMe)
---

# Blogs

Grouped by Tags To view by chronological order click [here]({{ site.github.repository_url }})

<p class="tag-cloud">
{% for tag in site.tags %}
<a class="tag" href="{{ site.github.repository_url }}/tags#{{ tag[0] }}">{{ tag[0] }}</a>
{% endfor %}
</p>

{% for tag in site.tags %}
  <h3 id="{{ tag[0] }}">{{ tag[0] }}</h3>
  <ul class="post-list">
    {% for post in tag[1] %}
      <li>
        <a class="post-list-title" href="{{ site.github.repository_url }}{{ post.url }}">{{ post.title }}</a>
        <div class="post-list-meta">
          <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time>
          {% for t in post.tags %}
            <a class="tag" href="tags#{{ t }}">{{ t }}</a>
          {% endfor %}
        </div>
        {% if post.desc %}
          <div class="post-list-desc">{{ post.desc }}</div>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
{% endfor %}

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
