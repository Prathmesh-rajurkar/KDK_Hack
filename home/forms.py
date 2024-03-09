from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=65)
    password=forms.CharField(max_length=65,widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username=forms.CharField(max_length=65)
    # firstname=forms.CharField(max_length=65)
    # lastname=forms.CharField(max_length=65)
    email=forms.EmailField(max_length=65)
    password=forms.CharField(max_length=65,widget=forms.PasswordInput)