from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import resolve
import datetime

class IndexView(generic.ListView):

    model = None
    template_name = 'homepage/index.html'

    id = 0
    context_object_name = 'query_set'

    def get_queryset(self):

        return "Er du GDPR COMPLIANT?"

class AboutView(generic.ListView):

    model = None

    template_name = 'homepage/about.html'
    id = 1
    context_object_name = 'query_set'

    def get_queryset(self):

        return "Om oss"


class AboutGDPRView(generic.ListView):

    model = None
    template_name = 'homepage/aboutGDPR.html'
    id = 2
    context_object_name = 'query_set'

    def get_queryset(self):

        return "Om GDPR"