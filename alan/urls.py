
'''from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework import routers
from api.views import TestViewSet


router =routers.DefaultRouter()
router.register(r'test', TestViewSet,base_name='test')

urlpatterns = [
    url(r'^api/', include('router.urls')),
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    
]'''

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'item', views.ItemViewSet,base_name='item')
router.register(r'marks', views.marksViewSet,base_name='marks')

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^alan/',views.datasave),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
