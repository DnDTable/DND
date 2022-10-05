from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404


def main(request):
    if request.user.is_authenticated:
        return redirect('users:profile')
    return render(request, 'registration/main.html')

def register(request):
    """Регистрирует нового пользователя"""
    msg = None
    success = False

    if request.user.is_authenticated:
        raise Http404

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect("users:login")
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = SignUpForm()

    return render(request, "registration/register.html", {"form": form, "msg": msg, "success": success})


def logon(request):
    """Логин пользователя в систему"""
    form = LoginForm(request.POST or None)
    msg = None

    if request.user.is_authenticated:
        raise Http404

    if not request.user.is_authenticated:
        if request.method == 'POST':

            if form.is_valid():
                user = authenticate(
                    username=request.POST.get('username'),
                    password=request.POST.get('password'))
                if user:
                    login(request, user)
                    return redirect('users:profile')
                else:
                    messages.error(request, 'Error validating form')

        context = {'form': form, 'msg': msg}
        return render(request, 'registration/login.html', context)

@login_required()
def profile(request):
    return render(request, 'registration/profile.html')