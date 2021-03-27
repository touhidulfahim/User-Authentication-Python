from django.shortcuts import render

# Create your views here.

def index(request):
    diction={'title':"Home Page"}
    return render(request,'LoginApp/index.html',context=diction)
