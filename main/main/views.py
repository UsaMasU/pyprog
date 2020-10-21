from django.http import HttpResponse
from django.shortcuts import render
from django_ajax.decorators import ajax

def index(request):
    template = 'index.html'

    if request.method == 'POST':
        print('post')
    else:  # request.method == 'GET'
        #area = request.GET.get('area')
        #get_area = lambda: f'WHERE [DeviceArea] = {area}' if area is not None else ""

        context = {
            'rows': 'rows',
            'text': 'Main Page',
        }
    return render(request, template, context)

@ajax
def my(request):
    c = 2 + 3
    return render(request, 'index.html')


