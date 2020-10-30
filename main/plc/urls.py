from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='plc_main'),
    path('one-get/', plc_one_get, name='plc_one_get'),
    path('test-save/', plc_get_data, name='plc_test_save'),
    path('reading-start/', plc_reading_start, name='plc_reading_start'),
    path('reading-stop/', plc_reading_stop, name='plc_reading_stop'),
]