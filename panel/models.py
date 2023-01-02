from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Iteam(models.Model):
    #мета опции
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'
        
     # поля модели   
    title = models.CharField(max_length=200, help_text="не более 200 символов", db_index=True)# настройки полей
    content = models.TextField(max_length=5000, blank=True, null=True, help_text="не более 5000 символов")
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)
    # методы модели
    def __str__(self):
        return self.title

