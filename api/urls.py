from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^notebook/$', views.ContactList.as_view()),
    url(r'^notebook/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view()),
    url(r'^notebook/search/(?P<chars>.+)$', views.contact_search),
]

urlpatterns = format_suffix_patterns(urlpatterns)
