from django import forms
from django.contrib.auth.models import User
from artgallery.models import *

class customerForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(help_text=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=['first_name','username','password']

    def clean(self):
        cleaned_data = super(customerForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")


        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class customerdetailform(forms.ModelForm):
    cus_name = forms.CharField(help_text='Same as your registered name')
    class Meta:
        model = Customer
        fields = '__all__'

class custproduct(forms.ModelForm):
    class Meta:
        model = Custpro
        fields= '__all__'

class ordersadmin(forms.ModelForm):
    class Meta:
        model = Orders
        exclude = ('status',)

class stockadmin(forms.ModelForm):
    class Meta:
        model = Stock
        fields= '__all__'

class purchaseadmin(forms.ModelForm):
    class Meta:
        model = Purchase
        fields= '__all__'

class reportadmin(forms.ModelForm):
    class Meta:
        model = Report
        fields= '__all__'