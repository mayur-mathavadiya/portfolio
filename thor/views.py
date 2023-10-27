from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import contact
def index(request):
  return render(request, "thor/index.html")


def contacte(request):
  a = request.POST['name']
  b = request.POST['email']
  c = request.POST['subject']
  d = request.POST['message']
  member = contact(name=a, email=b, subject=c, message=d)
  member.save()
  return HttpResponse('OK')
  # return response
