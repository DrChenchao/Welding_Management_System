from django.shortcuts import render

def index(request):
	return render(request,'INDEX/index.html')
def login(request):
	return render(request,'INDEX/login.html')


# Create your views here.s
