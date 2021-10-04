* [About Me](aboutMe)
---

# Blogs

Grouped by Tags To view by chronological order click [here]({{ site.github.repository_url }})

<ul>
    {% for tag in site.tags %}
          <span id="{{ tag[0] }}"><h3>{{ tag[0] }}</h3> </span>
		  <ul>
			{% for post in tag[1] %}
			  <li>{{ post.date | date: "%Y-%m-%d" }}: <a href="{{ site.github.repository_url }}{{ post.url }}">{{ post.title }}</a>
              <ul>
                {% if {{post.desc}} %}
                    <li> <em> {{ post.desc }} </em></li>
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
