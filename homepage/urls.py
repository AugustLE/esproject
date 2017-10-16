from django.conf.urls import url

from . import views

app_name = 'homepage'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/', views.AboutView.as_view(), name='about'),


]
