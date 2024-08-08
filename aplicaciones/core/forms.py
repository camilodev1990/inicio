from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User


<<<<<<< HEAD
# Formulario de registro de usuario
class SignUpForm(UserCreationForm):
=======
#formulario para crear un usuario
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'autocomplete': 'email'
        }),
        label=''  # Eliminar etiqueta
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
            'autocomplete': 'username'
        }),
        label=''  # Eliminar etiqueta
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'autocomplete': 'new-password'
        }),
        label=''  # Eliminar etiqueta
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
            'autocomplete': 'new-password'
        }),
        label=''  # Eliminar etiqueta
    )

>>>>>>> b60aa895ac455a0bc468875e56ebd6a01a18f119
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
<<<<<<< HEAD
    

#formulario de login
class CustomLoginForm(AuthenticationForm):
    pass

#formulario para recuperar contraseña
class CustomPasswordResetForm(PasswordResetForm):
=======


#formulario de login
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
            'autocomplete': 'username'
        }),
        label=''  # Eliminar etiqueta
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password'
        }),
        label=''  # Eliminar etiqueta
    )


#formulario para recuperar contraseña
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'autocomplete': 'email'
        }),
        label='Correo electrónico',
    )

>>>>>>> b60aa895ac455a0bc468875e56ebd6a01a18f119
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No existe un usuario con ese correo electrónico.")
        return email

<<<<<<< HEAD

# Formulario para confirmar contraseña antes de eliminar cuenta
class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

# Formulario para restablecer la contraseña
class CustomSetPasswordForm(SetPasswordForm):
    pass
=======
class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password'
        }),
        label=''
    )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nueva contraseña',
            'autocomplete': 'new-password'
        }),
        label='Nueva contraseña'
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmar nueva contraseña',
            'autocomplete': 'new-password'
        }),
        label='Confirmar nueva contraseña'
    )

#formulario para solicitud de contraseña para eliminar la cuenta
from django import forms

class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password'
        }),
        label=''
    )
>>>>>>> b60aa895ac455a0bc468875e56ebd6a01a18f119
