from django.contrib import admin
from Team.models import Desarrolladore

class DesarrolladoreAdmin(admin.ModelAdmin):
    list_display=("nombre","email","area","seniority","rating")
    search_fields=("nombre","email","area","lenguajes")
    list_filter=("disponible","seniority","ingles")
    ordering = ('-rating',)
    list_per_page=14
admin.site.register(Desarrolladore, DesarrolladoreAdmin)

