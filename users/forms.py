# CustomUserCreationForm is a form that you need to create in users/forms.py.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')  # Use password1 and password2 for password and password confirmation
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # No need to explicitly declare widgets for passwords - handled by UserCreationForm
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        # UserCreationForm handles password hashing in save method, so no need to manually set the password here
        if commit:
            user.save()
            
        return user
    
class CustomUserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'border-gray-300 focus:border-indigo-500 focus:ring-indigo-500 rounded-none rounded-r-md sm:text-sm border-2 p-3'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))  # PasswordInput for password fields

