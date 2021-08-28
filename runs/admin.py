from django.contrib import admin
from.models import *

# Register your models here.
@admin.register(Run)
class RunAdmin(admin.ModelAdmin):
    list_display=["id","user","date","start_at","end_at","distance","duration","speed","elevation"]

@admin.register(RunStamp)
class RunAdmin(admin.ModelAdmin):
    list_display=["id","run","start_at","end_at","distance","speed"]
