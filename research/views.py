from django.http import HttpResponse, HttpRequest
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic import View
from django.contrib import messages


def research_interests(request):
    return render(request, "research.html")
