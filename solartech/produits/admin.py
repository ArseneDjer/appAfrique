# your_app/admin.py
from django.contrib import admin
from .models import Product, EnergyMarketplace, EnergyExchange, Course, Sponsorship

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity_available', 'is_available')
    search_fields = ('name', 'description')
    list_filter = ('is_available',)

@admin.register(EnergyMarketplace)
class EnergyMarketplaceAdmin(admin.ModelAdmin):
    list_display = ('product', 'available_quantity', 'seller')
    search_fields = ('product__name', 'seller__username')
    list_filter = ('seller',)

@admin.register(EnergyExchange)
class EnergyExchangeAdmin(admin.ModelAdmin):
    list_display = ('user', 'energy_amount', 'date_shared', 'exchange_type')
    search_fields = ('user__username', 'exchange_type')
    list_filter = ('exchange_type',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_in_minutes', 'level')
    search_fields = ('title', 'level')
    list_filter = ('level',)

@admin.register(Sponsorship)
class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ('user', 'referred_user', 'date_joined')
    search_fields = ('user__username', 'referred_user__username')
