from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class InquilinoSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = CustomUser.UserType.INQUILINO
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
