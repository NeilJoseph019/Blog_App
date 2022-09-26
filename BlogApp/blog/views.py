from django.shortcuts import render

# Create your views here.
def indexPage(request):
    s = "Hello there lads "
    context = {
        "hello" : s
    }    
    return render(request,"blog/index.html", context)

def postsPage(request):
    pass

def postDetailPage(request):
    pass