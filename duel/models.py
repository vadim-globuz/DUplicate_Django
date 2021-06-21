from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    key = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.TextField(max_length=20, blank=True, verbose_name='Описание')
    cover = models.ImageField(upload_to='images/', verbose_name='Загрузка работы')
    rate = models.IntegerField(default=0, editable=False)
    loses = models.IntegerField(default=0, editable=False)
    voted_users = models.ManyToManyField(User, related_name='middleTab')

    def __str__(self):
        return self.title


class Organisation(models.Model):
    users = models.ManyToManyField(User, default='users', blank=True, related_name='users')
    admin_user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, null=True)
    organisation_name = models.TextField(max_length=20)
