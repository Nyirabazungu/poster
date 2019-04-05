from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home,name = 'welcome'),
    url(r'^profile/', views.profile,name='profile'),
    url(r'^profil/(\d+)',views.profil,name='profil'),
    url(r'^project/', views.project, name='project'),
    url(r'^projects/(\d+)',views.projects,name ='projects'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/project/$', views.ProjectList.as_view())
  


    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
