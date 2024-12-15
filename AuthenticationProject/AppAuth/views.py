from django.shortcuts import render, redirect
from .forms import CreateUserForm


# Create your views here.
def homepage(request):
    return render(request,'AppAuth/homepage.html')

def register(request):
    form  = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('my-login')
    
    return render(request,'AppAuth/register.html')

def my_login(request):
    return render(request,'AppAuth/my-login.html')

def dashboard(request):
    return render(request,'AppAuth/dashboard.html')
