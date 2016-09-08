from django.shortcuts import render

# Create your views here.

def index(request):
  template = 'hello/index.html'

  ip = request.META['REMOTE_ADDR']
  return render(request,template, {'dados': {'ip':ip}})