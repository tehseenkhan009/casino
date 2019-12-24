from django.contrib import admin
from .models import Casino


class CasinoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Casino, CasinoAdmin)