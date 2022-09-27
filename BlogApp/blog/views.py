from django.shortcuts import render

# Create your views here.
def indexPage(request):
    s = "Hello there lads, welcome to my blog ! "
    context = {
        "hello" : s
    }    
    return render(request,"blog/index.html", context)

def blogsPage(request):
    return render(request,"blog/blogsPage.html")

def blogDetailPage(request):
    pass