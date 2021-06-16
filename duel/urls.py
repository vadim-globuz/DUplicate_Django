from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('post/', views.post_new, name='add_post'),
    path('album/', views.album_view, name='album'),
    path('duels/', views.duel_get_works, name='duel'),
]
