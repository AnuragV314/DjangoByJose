from django.contrib import admin
from .models import *
# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = GroupMember

admin.site.register(Group)

