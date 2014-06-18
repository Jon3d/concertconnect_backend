from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from rest_framework import routers
from api import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'events', views.EventViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'concertconnect_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(url='http://www.google.com')),
    
    url(r'^api-rest-framework/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^ccadmin/', include(admin.site.urls)),
    
    url(r'^artist/$', views.Artists.as_view()),
    url(r'^artist/(?P<artist_name>)/$', views.Artists.as_view()),
)
