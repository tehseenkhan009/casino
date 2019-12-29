from django.contrib import admin
from .models import Casino, Bonus, Deals


class CasinoAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_recommended')
    ordering = ('name', 'is_recommended')
    pass


class BonusAdmin(admin.ModelAdmin):
    pass


class DealsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Casino, CasinoAdmin)
admin.site.register(Bonus, BonusAdmin)
admin.site.register(Deals, DealsAdmin)