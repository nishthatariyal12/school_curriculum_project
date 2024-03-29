from django import forms
from django.contrib.auth.models import User
from .models import user_profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")



class UserProfileInfoForm(forms.ModelForm):
    teacher='teacher'
    student='student'

    bio=forms.CharField(required=False)
    class Meta():
        model = user_profile
        fields=('bio','profile_picture')


