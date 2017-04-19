from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#	return HttpResponse("Rango says hello partner!<br/><a href='/rango/about/'>About</a>.")

def index(request):
	context_dict = {'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'rango/index.html', context=context_dict)


def about(request):
	context_dict = {'name':"Ievgen"}
	return render(request, 'rango/about.html', context=context_dict)