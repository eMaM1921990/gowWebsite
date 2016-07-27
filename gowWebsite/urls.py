"""gowWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from gate_of_world_app import views,api
from gowWebsite import settings

urlpatterns = [

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^sections/(?P<pk>[0-9]+)/$',views.categoryNews, name='categoryNews'),
    url(r'^lastnews/',views.latestNews, name='lastnews'),
    url(r'^article/(?P<pk>[0-9]+)/$',views.details, name='news'),



    ## apis
    url(r'^api/v1/fetchfeeds/$',api.fetchFeeds, name='fecthFeeds'),
]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


