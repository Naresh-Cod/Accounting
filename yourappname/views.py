from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm # Import your custom user creation form

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView  
from django.views.decorators.cache import never_cache

@never_cache
@login_required
def home(request):
    return render(request, 'home/index.html')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # Replace with your login template path
    authentication_form = CustomAuthenticationForm  # Use your custom authentication
    redirect_authenticated_user = True  # Redirect to home if already authenticated

class CustomSignupView(CreateView):
    form_class = CustomUserCreationForm  # Use your custom user creation form
    template_name = 'accounts/signup.html'  # Replace with your signup template path
    success_url = reverse_lazy('login')  # Redirect to login page upon successful signup

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)  # Automatically log in the user upon successful signup
        return response


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def restricted_view(request):
    return render(request, 'restricted.html')

@never_cache
def user_logout(request):
    logout(request)
    return redirect('login')

