from django.conf.urls import url

from . import views

app_name = 'homepage'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^aboutUs/$', views.AboutView.as_view(), name='aboutUs'),
    url(r'^aboutGDPR/$', views.AboutGDPRView.as_view(), name='aboutGDPR'),
    url(r'^checklists/$', views.ChecklistView.as_view(), name='checklists'),
    url(r'^confirmation/(?P<anystring>.+)/$', views.ConfirmationView.as_view(), name='confirmation'),
    url(r'^sendChecklist/$', views.sendInChecklist, name='sendChecklist'),

]
