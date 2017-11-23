from django.conf.urls import url, include

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as rest_framework_views
#from esproject.urls import urlpatterns

app_name = 'rest'

urlpatterns = [

    url(r'^checklists/$', views.ChecklistList.as_view()),
    url(r'^checklists/(?P<pk>[0-9]+)$', views.CheckListDetail.as_view()),
    url(r'^checklists/answers/$', views.ChecklistAnswerList.as_view()),
    url(r'^checklists/answers/(?P<email>.+)/$', views.ChecklistAnswersUser.as_view()),
    url(r'^checklists/answer/(?P<pk>.+)/$', views.ChecklistAnswerDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^login/$', views.UserAuth.as_view()),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'^user/login/$', views.UserAuthToken.as_view(), name='login'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





urlpatterns = format_suffix_patterns(urlpatterns)
