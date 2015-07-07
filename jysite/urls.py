"""jysite URL Configuration

"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('activity.urls')),
    url(r"^help$", TemplateView.as_view(template_name='help.html'), name="help"),
    url(r"^about$", TemplateView.as_view(template_name='about.html'), name="about"),
    url(r"^privacy$", TemplateView.as_view(template_name='privacy.html'), name="privacy"),
    url(r"^terms$", TemplateView.as_view(template_name='terms.html'), name="terms"),
    url(r"^contact$", TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    #urls for social accounts

    url(r'^accounts/', include('allauth.urls')),
]

if settings.DEBUG:
   urlpatterns += [
       url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
       'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
       url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:],
       'django.views.static.serve',
       {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
   ]
