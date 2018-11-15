from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework_swagger.views import get_swagger_view

from apps.accounts.views import ActivateByGet

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('tasks.api.urls')),
    url(r'^schema/$', schema_view),

    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    path('activate/<str:uid>/<str:token>/', ActivateByGet.as_view()) #<str:uid>/<str:token>/
]

if settings.DEBUG:
    from django.conf.urls.static import static

    # Serve static and media files from development server
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Simple Tasks Admin'
