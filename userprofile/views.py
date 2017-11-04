from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

class ProfileView(generic.ListView):

    model = None
    template_name = 'userprofile/profile.html'

    id = 0
    context_object_name = 'query_set'

    def get_queryset(self):

        return [""]


class ChecklistView(generic.ListView):

    model = None
    template_name = 'userprofile/user-checklists.html'

    id = 1
    context_object_name = 'query_set'

    def get_queryset(self):

        return [""]

