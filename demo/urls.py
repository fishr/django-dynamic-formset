import django
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^examples/', include('example.urls')),
]

try:
    import ajax_select
    # If django-ajax-selects is installed, include its URLs:
    urlpatterns += [
        url(r'^ajax_select/', include('ajax_select.urls')),
    ]
except ImportError:
    pass

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root= settings.MEDIA_ROOT)
