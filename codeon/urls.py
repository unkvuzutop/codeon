from django.conf.urls import include, url
from django.contrib import admin

from students import urls as student_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(student_urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
]
