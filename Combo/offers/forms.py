from django import forms

from .models import Product_Form

class MyModelForm(forms.ModelForm):

    class Meta:
        model = Product_Form
        fields=['lower_limit','upper_limit','email','file1']