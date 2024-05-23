
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rooms/', include('rooms.urls')),
    path('search/', views.user_search_view, name='user_search'),
    path('', include('core.urls', namespace=''))
]
