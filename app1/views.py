from django.shortcuts import render

def app_view(request):
  return render(request,"app1/app.html")