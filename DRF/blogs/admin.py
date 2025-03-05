from django.contrib import admin
from blogs.models import * 
# Register your models here.

admin.site.register(Blog)
admin.site.register(Comment)