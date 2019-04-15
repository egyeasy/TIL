# 27homework

1. ```python
   class PostCreate(LoginRequiredMixin, CreateView):
       model = Post
       fields = '__all__'
   ```

2. ```python
   from django.db import models
   from django.conf import settings
   
   class Question(models.Model):
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       title = models.CharField(max_length=50)
       
   	def __str__(self):
           return self.title
   ```

