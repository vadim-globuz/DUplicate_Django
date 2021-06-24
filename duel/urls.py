from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('post/', views.post_new, name='add_post'),
    path('album/', views.album_view, name='album'),
    path('duels/', views.duel_get_works, name='duel'),
    path('leaderboard/', views.leaderboards, name='top'),
    path('organisations_add/', views.organisation_new, name='org_add'),
    path('organisations_enter/', views.enter_org, name='org_enter'),
    path('organisations/', views.org_menu, name='org_menu'),
    path('organisations_duel/', views.duel_get_works_organisation, name='org_duel')
]
