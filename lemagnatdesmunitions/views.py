from django.shortcuts import render

#simple function which return the index page
def index(request):
	return render(request, 'index.html', locals())

def loaderio(request):
	return render(request, 'loaderio.html', locals())