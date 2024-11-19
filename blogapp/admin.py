from django.contrib import admin
from blogapp.models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin): 
    list_display = ('title', 'type', 'is_active') 
    list_filter = ('is_active', 'type') 
    search_fields = ('title', 'content')
admin.site.register(Blogpost,BlogAdmin)