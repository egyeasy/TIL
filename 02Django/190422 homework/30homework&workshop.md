# 30homework

1. `ManyToManyField`
2. `related_name`



# 30workshop

```python
from django.db import models


class Hashtag(models.Model):
    content = models.TextField()


class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    hashtag = models.ManyToManyField(Hashtag, related_name="post", blank=True)
```

