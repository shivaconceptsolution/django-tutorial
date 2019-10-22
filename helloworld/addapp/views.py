from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return render(request,"addapp/index.html")
def addlogic(request):
    a = request.GET["txtnum1"]
    b = request.GET["txtnum2"]
    c= int(a)+int(b)
    return HttpResponse("result is "+str(c))	

