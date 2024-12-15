from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')

    context = {'title': 'Register', 'form': form}
    return render(request, 'register.html', context=context)
def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request=request, user=form.get_user())
            return redirect('home')
    
    context = {'title': 'Login','form': form}
    return render(request,'login.html',context=context)
def logout(request):
    if request.method == 'POST':
        logout(request)
        return render(request,"logout.html")

def home(request):
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_page = "home"
    
    