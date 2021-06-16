
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from DIPLOM_DUEL import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('duel.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)