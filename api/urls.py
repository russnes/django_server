# file: api/urls.py

from django.conf.urls import url, include
from rest_framework.authtoken import views as drf_views
from rest_framework import routers
from api import views


PREFIX='am_rockin/'

router = routers.SimpleRouter()
router.register(r'test', views.TestModelViewSet)

app_name="api"

urlpatterns = [
    url(r'auth$', drf_views.obtain_auth_token, name='auth'),
    url(r'api/', include(router.urls)),
]

#urlpatterns += router.urls
