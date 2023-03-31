from django.contrib import admin
from .models import *

# Register your models here.

class CodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'created_at', 'quantity', 'active')
    list_editable = ('active',)
    readonly_fields = ('created_at',)
admin.site.register(Code, CodeAdmin)