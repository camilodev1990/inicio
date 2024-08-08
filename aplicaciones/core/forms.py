from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User


# Formulario de registro de usuario
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    

#formulario de login
class CustomLoginForm(AuthenticationForm):
    pass

#formulario para recuperar contraseña
class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No existe un usuario con ese correo electrónico.")
        return email


# Formulario para confirmar contraseña antes de eliminar cuenta
class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

# Formulario para restablecer la contraseña
class CustomSetPasswordForm(SetPasswordForm):
    pass
