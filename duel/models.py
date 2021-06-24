from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    key = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.TextField(max_length=20, blank=True, verbose_name='Описание')
    cover = models.ImageField(upload_to='images/', verbose_name='Загрузка работы')
    rate = models.IntegerField(default=0, editable=False)
    loses = models.IntegerField(default=0, editable=False)
    voted_users = models.ManyToManyField(User, related_name='middleTab', null=True)
    organisation_rate = models.IntegerField(default=0, editable=False)
    organisation_loses = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title


class Organisation(models.Model):
    org_name = models.TextField(max_length=20, verbose_name='Название организации')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Администратор')
    vote_type = models.BooleanField(default=False, verbose_name='Каждая работа c каждой')

    def __str__(self):
        return self.org_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    org = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True, default=0, null=True)
