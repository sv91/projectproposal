"""
URL file for the main project "Project proposal"
"""
from django.conf.urls import include, url
from django.contrib import admin


# Defines the different possible paths.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^formular/', include('formular.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
