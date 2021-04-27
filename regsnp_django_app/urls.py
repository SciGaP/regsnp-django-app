from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

app_name = 'regsnp_django_app'
urlpatterns = [
    url(r'^expviz/', views.expviz, name="expviz"),
    url(r'^splicetable/', views.splice_res, name="splice"),
    #url(r'^languages/', views.languages, name="languages"),
] 
