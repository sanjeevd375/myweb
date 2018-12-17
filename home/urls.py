#Home URLS

from django.conf.urls import url
from .import views

urlpatterns = [
    url('^intro/marlabs',views.marlabs),
    url('^intro/$', views.home),
    url('^json/$',views.fbview),
    #url('^excel/',views.details),
    
]

print (urlpatterns)
