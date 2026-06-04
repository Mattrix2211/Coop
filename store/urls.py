from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Produits
    path('products/', views.product_list, name='product_list'),
    path('products/new/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('products/<int:pk>/add-stock/', views.product_add_stock, name='product_add_stock'),
    path('products/<int:pk>/adjust-stock/', views.product_adjust_stock, name='product_adjust_stock'),
    path('stocks/movements/', views.stock_movements_list, name='stock_movements_list'),
    path('products/bulk-move/', views.product_bulk_move, name='product_bulk_move'),

    # Catégories
    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('categories/new/ajax/', views.category_create_ajax, name='category_create_ajax'),
    path('categories/<int:pk>/delete/ajax/', views.category_delete_ajax, name='category_delete_ajax'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Clients
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/new/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customers/<int:pk>/bulk-payment/', views.bulk_settle_customer, name='bulk_settle_customer'),

    # Ventes
    path('sales/', views.sale_list, name='sale_list'),
    path('sales/new/', views.sale_create, name='sale_create'),
    path('sales/<int:pk>/receipt/', views.sale_receipt_fragment, name='sale_receipt_fragment'),
    path('sales/<int:pk>/pay/', views.pay_sale, name='pay_sale'),
    path('sales/confirm/', views.sale_confirm, name='sale_confirm'),
    path('sales/<int:pk>/payment/', views.add_payment, name='add_payment'),
    path('sales/<int:pk>/receipt.pdf', views.sale_receipt_pdf, name='sale_receipt_pdf'),
    path('sales/clear/', views.clear_sales_history, name='clear_sales_history'),
    path('sales/<int:pk>/delete/', views.sale_delete, name='sale_delete'),

    # Dettes et exports
    path('debts/', views.debts_list, name='debts_list'),
    path('debts/customers/', views.debt_customers_list, name='debt_customers_list'),
    path('exports/sales.xlsx', views.export_sales_xlsx, name='export_sales_xlsx'),
    path('exports/debts.xlsx', views.export_debts_xlsx, name='export_debts_xlsx'),
    path('exports/debtors.xlsx', views.export_debtors_xlsx, name='export_debtors_xlsx'),
    path('exports/products.xlsx', views.export_products_xlsx, name='export_products_xlsx'),

    # Caisse
    path('cash/', views.cash_dashboard, name='cash_dashboard'),
    path('cash/reset/', views.cash_reset, name='cash_reset'),
    path('cash/drop/', views.cash_drop, name='cash_drop'),
    path('cash/exports/movements.xlsx', views.export_cash_movements_xlsx, name='export_cash_movements_xlsx'),
]