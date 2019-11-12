from django.shortcuts import render
from .forms import NumForm
# Create your views here.

def numform(request):
    numform = NumForm()
    params = {
        'numform': numform
    }
    return render(request, 'result.html', params)

