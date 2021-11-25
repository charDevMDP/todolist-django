"""todo URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from apps.app.views import TaskViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('', include('apps.app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls))

]
