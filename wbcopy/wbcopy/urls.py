from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from wbchina.views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wbchina.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', custom_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
