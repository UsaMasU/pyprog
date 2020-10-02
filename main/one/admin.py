from django.contrib import admin
from .models import *

class OtherObjectsInRequestInline(admin.TabularInline):
    model = OtherObjectsInRequest
    extra = 1

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    inlines = (OtherObjectsInRequestInline,)

@admin.register(Valve)
class ValveAdmin(admin.ModelAdmin):
    pass

@admin.register(Motor)
class MotorAdmin(admin.ModelAdmin):
    pass

@admin.register(OtherObject)
class OtherObjectAdmin(admin.ModelAdmin):
    inlines = (OtherObjectsInRequestInline,)
