from django.conf.urls import url

from . import views

app_name = 'userprofile'

urlpatterns = [

    url(r'^profile$', views.ProfileView.as_view(), name='profile'),
    url(r'^yourChecklists', views.ChecklistView.as_view(), name='checklists'),


]