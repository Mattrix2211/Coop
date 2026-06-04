from django.contrib import admin
from .models import Product, Customer, Sale, SaleItem, Payment, Category, CashSession, CashMovement


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ("name", "category", "price", "quantity")
	search_fields = ("name",)
	list_filter = ("category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name",)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name")
	search_fields = ("first_name", "last_name")


class SaleItemInline(admin.TabularInline):
	model = SaleItem
	extra = 0


class PaymentInline(admin.TabularInline):
	model = Payment
	extra = 0


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
	list_display = ("id", "customer", "created_at", "total", "amount_paid", "balance")
	inlines = [SaleItemInline, PaymentInline]


@admin.register(CashSession)
class CashSessionAdmin(admin.ModelAdmin):
	list_display = ("id", "opened_at", "is_closed", "closed_at")
	readonly_fields = ("opened_at", "closed_at")
	search_fields = ("id",)


@admin.register(CashMovement)
class CashMovementAdmin(admin.ModelAdmin):
	list_display = ("id", "session", "movement_type", "method", "amount", "created_at")
	list_filter = ("movement_type", "method")
	search_fields = ("note",)

# Personnalisation de l'interface d'administration en français
admin.site.site_header = "Administration Coop"
admin.site.site_title = "Administration Coop"
admin.site.index_title = "Gestion du magasin"
