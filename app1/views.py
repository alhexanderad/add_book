from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from app1.models import Book

def app_view(request):
  return render(request,"app1/app.html")

def saveBook(request):
  if request.is_ajax():
    name = request.POST.get('name')
    prize = request.POST.get('prize')
    pages = request.POST.get('pages')
    
    book = Book.objects.create(name=name, prize=prize, pages=pages)
    try:
      book.save()
      print("se gravob")
    except :
      print(":(")
      
    data ={
      'name':name,
    }
    print(name)
    print(request.POST.get('prize',None))
    print(request.POST.get('pages',None))
    return JsonResponse(data)
  return HttpResponse("<h1>XD</h1>")
