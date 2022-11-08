from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('about/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
]
