from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path
from rest_framework import routers

from robots.viewsets import *

router = routers.DefaultRouter()
router.register(r'robots', RobotViewSet)
router.register(r'danceoffs', DanceoffViewSet)
router.register(r'battles', BattleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
    ))
]
