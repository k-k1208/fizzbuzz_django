from django.shortcuts import render
from .forms import NumForm#htmlのinputで事足りるからいらん
# Create your views here.

def numform(request):
    return render(request, 'num_form.html')

def result(request):
    print(request.POST)
    numform = request.POST['number']
    params = {
        'numform': numform
    }
    return render(request, 'result.html', params)
