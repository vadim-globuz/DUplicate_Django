from django.contrib.auth import views
from django.urls import path, reverse_lazy
from .views import register

app_name = 'login'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', register, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_reset/', views.PasswordResetView.as_view(
        success_url=reverse_lazy('login:password_reset_done')
    ), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('login:password_reset_complete')
    ), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
