from django import forms
from .models import Report
from .models import Customer
import re

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    re_password = forms.CharField(widget=forms.PasswordInput, label='Re-enter Password')


    class Meta:
        model = Customer
        fields = ['name','email','location', 'mobile_number', 'password', 're_password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Invalid email format")
        return email

    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if not re.match(r"^\d{10,15}$", mobile_number):
            raise forms.ValidationError("Invalid mobile number format")
        return mobile_number

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.search(r"[A-Z]", password):
            raise forms.ValidationError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", password):
            raise forms.ValidationError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", password):
            raise forms.ValidationError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise forms.ValidationError("Password must contain at least one special character")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password and password != re_password:
            raise forms.ValidationError("Passwords do not match")





class RentalForm(forms.Form):
    # This form will handle vehicle rental, you can customize it as needed
    pass  # Implement as necessary

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['description']



