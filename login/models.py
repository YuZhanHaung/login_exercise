from django.db import models

# Create your models here.

class User(models.Model):

    gender = (
        ('male','male'),
        ('female','female')
    )
    name = models.CharField(max_length=128,unique=True,verbose_name='username')
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(choices=gender,max_length=32, default='male')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = 'user'
        verbose_name_plural = 'users'

