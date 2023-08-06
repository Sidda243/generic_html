from django.shortcuts import render

# Create your views here.

def table(request):
    return render(request,'table.html')

def img_rotate(request):
    return render(request,'img_rotate.html')

def nav(request):
    return render(request,'nav.html')

def img(request):
    return render(request,'img.html')
def a_response(request):
    return render(request,'a_response.html')

def x(request):
    return render(request,'x.html')

def reg_form(request):
    return render(request,'reg_form.html')

def new(request):
    return render(request,'new.html')

def box(request):
    return render(request,'box.html')

def arth(request):
    return render(request,'arth.html')

def appli(request):
    return render(request,'appli.html')

def jsp(request):
    return render(request,'jsp.html')

def jsp1(request):
    return render(request,'jsp1.html')

def amz(request):
    return render(request,'amz.html')

def form(request):
    return render(request,'form.html')

def convert(request):
    return render(request,'convert.html')