# 20homework

1. ```python
   class Student(models.Model):
       name = models.TextField()
       num_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="students")
   ```

2. ```python
   comments = A.comment_set.all()
   ```

3. `movie_id`



# 20workshop

### models.py

```python
from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)

class Choice(models.Model):
    content = models.CharField(max_length=20)
    votes = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
```

