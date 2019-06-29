# 26homework

1. `from django import forms`

2. ```html
   {% extends 'base.html' %}
   
   {% load bootstrap4 %}
   
   {% block body %}
   <h1>새로운 Post 작성하기</h1>
   <form method="POST" enctype="multipart/form-data">
     {% csrf_token %}
     {{ form.as_p }}
     {% buttons %}
       <button type="submit" class="btn btn-primary">업로드</button>
     {% endbuttons %}
   </form>
   {% endblock %}
   ```

3. `cleaned_data`



# 26workshop

1. ```python
   from django import forms
   from .models import Student
   
   class StudentForm(forms.Form):
       name = forms.CharField(max_length=100)
   	age = forms.IntegerField()
   ```

2. ```html
   <form method="POST" action="/students/create/">
       {% csrf_token %}
       {{ form.as_p }}
       <input type="submit">
   </form>
   ```

