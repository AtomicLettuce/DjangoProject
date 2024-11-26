from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname","joined_date","id")

# Register your models here.
admin.site.register(Member, MemberAdmin)



