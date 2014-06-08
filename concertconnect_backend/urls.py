from django.conf.urls import patterns, include, url

from rest_framework import routers
from api import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'add_artist', views.GroupViewSet)
router.register(r'remove_artist', views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cc_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
)
