# 21homework

1. ```html
   {%extends 'base.html' %}
   
   {% block body_block %}
   <h1>{{question.title}}</h1>
   <h1>{{question.author}}</h1>
   
   {% for comment in question.comment_set.all %}
   	<h3>{{comment.content}}</h3>
   {% endfor %}
   
   {% endblock %}
   ```

2. `<form action="{% url 'question:comments_create' question.id %}">`



# 21workshop

```html
<h1>{{question.title}}</h1>
<ul>
    {% for choice in question.choice_set.all %}
    	<li>{{choice.content}} : {{choice.votes}}</li>
    {% endfor %}
</ul>
```

