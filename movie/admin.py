from django.contrib import admin
from .models import Movie,Email
# Register your models here.
admin.site.register(Movie)

@admin.register(Email)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','emailid')