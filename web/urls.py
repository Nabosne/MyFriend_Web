from django.conf.urls import url
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns = [
    url('service/ondeestou/', OndeEstou.as_view()),
    url('service/descrever/', DescreverLocal.as_view()),
    url('service/destinos/', Destinos.as_view()),
    url('service/locais/', Locais.as_view())
]