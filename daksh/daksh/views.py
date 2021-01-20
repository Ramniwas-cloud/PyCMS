# I have created this website - Riky

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	params = {'name':'ricky','place':'Ghaziabad'}
	return render(request,'index.html', params)
	# return HttpResponse("hello")
	#return HttpResponse('''<h1>This is Ricky</h1> <a href="https://www.youtube.com/">Link to //// Youtube</a>''')

def about(request):
	print(request.GET.get('fname', 'default'))
	return HttpResponse(" About Hello <a href='/'>Back</a>")

def products(request):
	 return HttpResponse("About Products <a href='/'>back</a>")

def contact(request):
	 return HttpResponse("About contact <a href='/'>bacK</a>")