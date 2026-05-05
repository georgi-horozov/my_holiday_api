from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

UserModel = get_user_model()


class MyHolidayUserCreationForm(auth_forms.UserCreationForm):
    user = None

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords do not match!")

            validate_password(password2)

        return cleaned_data

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

class MyHolidayUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
