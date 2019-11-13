from django.shortcuts import render
from .forms import NumForm
# Create your views here.

def numform(request):
    numform_by_forms = NumForm()  # forms.Formで作ったform
    params = {
        'numform_by_forms': numform_by_forms
    }
    return render(request, 'num_form.html', params)

def result(request):
    print(request.POST)
    numform = int(request.POST['num'])
    comment = request.POST['comment']

    result_list = []
    for i in range(1, numform+1):
        judge = fizz_buzz_judge(i)
        result_list.append(judge)
    params = {
        'numform': numform,
        'comment': comment,
        'result_list': result_list
    }
    return render(request, 'result.html', params)




def fizz_buzz_judge(x):

    if x % 15 == 0:
        judge = 'FIZZBUZZ'
    elif x % 5 == 0:
        judge = 'Buzz'
    elif x % 3 == 0:
        judge = 'Fizz'
    else:
        judge = str(x)
    return judge


