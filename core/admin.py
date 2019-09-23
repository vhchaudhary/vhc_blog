
from django.contrib import admin
from .models import *


class TeachInline(admin.TabularInline):
    model = Technology


class CategAdmin(admin.ModelAdmin):
    inlines = [TeachInline]


admin.site.register(Blog)
admin.site.register(Technology)
admin.site.register(Category, CategAdmin)
admin.site.register(Author)