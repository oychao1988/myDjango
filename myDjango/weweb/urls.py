from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^get_params_from_url_regex/(\w+)/(\d{4})$', views.get_params_from_url_regex),
    url(r'^get_params_from_url_name/(?P<a>\w+)/(?P<b>\d{4})$', views.get_params_from_url_name),
    url(r'^get_params_from_request/$', views.get_params_from_request),
    url(r'^get_params_from_form/$', views.get_params_from_form),
    url(r'^set_cookie/$', views.set_cookie),
    url(r'^get_cookie/$', views.get_cookie),
]