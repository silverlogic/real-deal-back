from django.contrib import admin

from .models import Merchant, Offer, MerchantOffer


class MerchantOfferInline(admin.TabularInline):
    model = MerchantOffer


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [MerchantOfferInline]


class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description',)
    inlines = [MerchantOfferInline]


admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Offer, OfferAdmin)
