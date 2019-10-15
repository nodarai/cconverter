from django.contrib import admin

from convert.models import Currency, CurrencyRate


def custom_titled_filter(title):
    class Wrapper(admin.RelatedFieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


class CurrencyAdmin(admin.ModelAdmin):
    fields = ('code', 'full_name')
    list_display = ('code', 'full_name')
    list_filter = ('code', 'full_name')


class CurrencyRateAdmin(admin.ModelAdmin):
    fields = ('convert_from', 'convert_to', 'rate')
    list_display = ('convert_from', 'convert_to', 'rate', 'created_at')
    list_filter = (
        ('convert_from__code', custom_titled_filter('from currency')),
        ('convert_to__code', custom_titled_filter('to currency')),
    )


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(CurrencyRate, CurrencyRateAdmin)
