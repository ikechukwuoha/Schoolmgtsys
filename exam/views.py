from django.shortcuts import render

# Create your views here.

def index(request):
    
    
    context = {}
    return render(request, 'exam/index.html', context)



def examination(request):
    
    first_num = int(request.GET['num1'])
    second_num = int(request.GET['num2'])
    res = first_num + second_num
    
    return render(request, 'exam/examination.html', {'result': res})