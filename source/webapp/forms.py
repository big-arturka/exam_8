from django import forms
from webapp.models import Product, Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'image']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-input'}),
                   'description': forms.Textarea(attrs={'class': 'form-area'}),
                   'category': forms.Select(attrs={'class': 'form-select'}),
                   }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['description', 'rating']
        widgets = {'description': forms.Textarea(attrs={'class': 'form-area'}),
                   'rating': forms.Select(attrs={'class': 'form-select'})
                   }