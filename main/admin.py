from django.contrib import admin
from main.models import *
# Register your models here.


class QueryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'query']
    search_fields = ('name', 'email', 'query')
    list_filter = ['active', 'created']


admin.site.register(Query, QueryAdmin)
