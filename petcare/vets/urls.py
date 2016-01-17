from django.conf.urls import url


from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^find/',views.search,name='search'),
    url(r'^searchtomap/',views.searchtomap,name='searchtomap'), 
    url(r'^locate/(?P<lat>\d*[.]?\d+)/(?P<lon>\d*[.]?\d+)',views.url_extract,name='check'),  
    url(r'^locate/',views.locate_me,name='locate'),


]