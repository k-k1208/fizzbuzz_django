from django.shortcuts import render
# Create your views here.

def numform(request):
    return render(request, 'num_form.html')

def result(request):
    numform = int(request.POST['number'])
    result_list = []
    for i in range(1, numform+1):
        judge = fizz_buzz_judge(i)
        result_list.append(judge)
    params = {
        'numform': numform,
        'result_list': result_list,
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


