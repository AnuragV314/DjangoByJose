from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'email')
    search_fields = ('first_name',)
    # list_editable = ('',)
    # list_filter = ('',)


admin.site.register(User, UserAdmin)
