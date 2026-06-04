from django import forms
from django.forms import inlineformset_factory
from .models import Product, Customer, Sale, SaleItem, Payment, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "price", "quantity", "min_stock", "image"]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name"]


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["customer", "note"]
        widgets = {
            "customer": forms.Select(attrs={"class": "form-select form-select-sm"}),
            "note": forms.Textarea(attrs={"placeholder": "Note (optionnel)", "rows": 2})
        }


class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ["product", "quantity", "unit_price"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-select form-select-sm"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control form-control-sm text-center", "style": "width: 80px"}),
            # on masque le champ dans l'UI, il reste soumis et manipulé par le JS
            "unit_price": forms.HiddenInput(),
        }


SaleItemFormSet = inlineformset_factory(
    Sale,
    SaleItem,
    form=SaleItemForm,
    fields=["product", "quantity", "unit_price"],
    extra=1,
    can_delete=True
)
