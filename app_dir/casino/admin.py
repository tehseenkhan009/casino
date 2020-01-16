from django.contrib import admin
from .models import Casino, Bonus, Deals, CountryUrl, Country
from adminsortable.admin import SortableAdmin


class CasinoAdmin(SortableAdmin):
    list_display = ('name', 'is_recommended')
    ordering = ('name', 'is_recommended')


class BonusAdmin(admin.ModelAdmin):
    pass


class DealsAdmin(SortableAdmin):
    def get_object(self, request, object_id, s):
        self.obj = super(DealsAdmin, self).get_object(request, object_id)
        return self.obj

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "url_country":
            kwargs["queryset"] = CountryUrl.objects.filter(casino=self.obj.casino.id)
        return super().formfield_for_manytomany(db_field, request, **kwargs)


class CountryAdmin(SortableAdmin):
    pass


class CountryUrlAdmin(SortableAdmin):
    pass


admin.site.register(Casino, CasinoAdmin)
admin.site.register(Bonus, BonusAdmin)
admin.site.register(Deals, DealsAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(CountryUrl, CountryUrlAdmin)