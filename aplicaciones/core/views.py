from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views import View
from django.views.generic.edit import CreateView
from .forms import ConfirmPasswordForm, CustomLoginForm, SignUpForm, CustomPasswordResetForm



#vista base
def base(request):
    return render(request, 'base.html')

#vista ingreso
class CustomLoginView(LoginView):
    form_class = CustomLoginForm

#vista registro
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = '/login/'
    template_name = 'signup.html'

#vista confirmar cerrar sesion
@method_decorator(login_required, name='dispatch')
class ConfirmLogoutView(View):
    template_name = 'confirm_logout.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        logout(request)
        return redirect('base')
    
#vista para recuperar contraseña
def custom_password_reset(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            return redirect('password_reset_done')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': form})


#vista para eliminar cuenta
@login_required
def delete_account(request):
    if request.method == 'POST':
        form = ConfirmPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            user = authenticate(username=request.user.username, password=password)
            if user is not None:
                request.user.delete()
                messages.success(request, 'Cuenta eliminada exitosamente')
                return redirect('base')
            else:
                messages.error(request, 'Contraseña incorrecta. Por favor, inténtelo de nuevo.')
    else:
        form = ConfirmPasswordForm()
    
    return render(request, 'delete_account.html', {'form': form})