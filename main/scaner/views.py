from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Scan
from .forms import ScanForm

class ScanViews(ListView):
    model = Scan
    #template_name = ''
    #context_object_name = ''
    #extra_context = {'title': 'Scan views'}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Views'
        return context

    def get_queryset(self):
        return Scan.objects.all()


class ScanCreate(CreateView):
     form_class = ScanForm
     template_name = 'scaner/add_scan.html'


def scan_add(request):
    if request.method == 'POST':
        form = ScanForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['code'])
            #scan = Scan.objects.create(**form.cleaned_data)
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = ScanForm
    context = {
        'form': form,
        'object_list': Scan.objects.order_by('-pk')
    }
    return render(request, 'scaner/add_scan.html', context)


def index(request):
    template = 'scaner/index.html'

    if request.method == 'POST':
        print('post')
    else:  # request.method == 'GET'
        #area = request.GET.get('area')
        #get_area = lambda: f'WHERE [DeviceArea] = {area}' if area is not None else ""

        context = {
            'rows': 'rows',
            'text': 'Scaner',
        }
    return render(request, template, context)

