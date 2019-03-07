"""airbuzz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from airbuzz import views

app_name = 'airbuzz'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.indexView),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^signout/$', views.signout, name="signout"),
    url(r'^dashboard/$', views.dashboardRedirect),
    url(r'^user/(?P<username>[\w_]{3,50})/dashboard$', views.dashboardView, name="dashboard"),
    url(r'^user/(?P<username>[\w_]{3,50})/a320$', views.a320View, name="a320"),
    url(r'^user/(?P<username>[\w_]{3,50})/a330$', views.a330View, name="a330"),
    url(r'^user/(?P<username>[\w_]{3,50})/a350$', views.a350View, name="a350"),
    url(r'^user/(?P<username>[\w_]{3,50})/search$', views.searchView, name="search"),
    url(r'^user/(?P<username>[\w_]{3,50})/edit/$', views.editProfileView, name="edit-profile"),
]
