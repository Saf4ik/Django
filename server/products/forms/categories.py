from django import forms
from products.models import Category


# class CategoryForm(forms.Form):
#     name = forms.CharField(max_length=255, required=True)
#     description = forms.CharField(
#         required=False,
#         widget=forms.widgets.Textarea(attrs={'class': 'category-description'})
#     )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.widgets.TextInput(attrs={'class': 'name-field'}),
            'discription': forms.widgets.Textarea(attrs={'class': 'description-field'}),
        }