from django.contrib import admin

from .models import Movie, Customer
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    fields= ['release_year', 'titel', 'length']
    search_fields = ['titel']
    list_filter = ['release_year', 'length']
    list_display = ['release_year', 'titel', 'length']
    list_editable = ['titel']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Customer)
