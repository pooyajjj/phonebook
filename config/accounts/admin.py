from django.contrib import admin

from .models import phonenum

# Register your models here.

class phonenumAdmin(admin.ModelAdmin):
    list_display = ('name','phone_num')


admin.site.register(phonenum,phonenumAdmin)