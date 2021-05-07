from django.shortcuts import render
def showmain(request):
    return render(request, 'main/mainpage.html')

def childhood(request):
    return render(request, 'main/childhood.html')

def teenager(request):
    return render(request, 'main/teenager.html')

def adult(request):
    return render(request, 'main/adult.html')

# Create your views here.
