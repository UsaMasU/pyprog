from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='plc_main'),
    #path('views/', ScanViews.as_view(), name='scan_views'),
    #path('scan/<int:scan_id>', index, name='scan'),
    #path('scan-add/', scan_add, name='scan_add'),
    #path('scan-add/', ScanCreate.as_view(), name='scan_add'),

]