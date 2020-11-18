from django import forms
from products.models import Product, Manufactorer, CaroPics
from django.forms import ModelForm

# We're in prdMgt forms.


class AddProductForm(ModelForm):
    prefix = 'addproduct'

    class Meta:
        model = Product
        fields = ('category', 'manufactorer', 'name', 'description',
                  'price', 'image', 'stock', 'available', 'latest', 'best',)


class AddBrandForm(ModelForm):
    prefix = 'addbrand'

    class Meta:
        model = Manufactorer
        fields = ('name',)


class AddSideForm(ModelForm):
    class Meta:
        model = CaroPics
        fields = ('product', 'image',)


class ProdList(forms.Form):
    lookupProd = forms.ModelChoiceField(label="Product",
                                        queryset=Product.objects.all()
                                        .order_by(
                                            'name'),
                                        empty_label="(Select Product)",
                                        widget=forms.Select(attrs={
                                            'onchange':
                                            'this.form.submit();'}))


class EditProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'manufactorer', 'name', 'description',
                  'price', 'image', 'stock', 'available', 'latest', 'best',)
