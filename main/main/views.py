from django.shortcuts import render

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
