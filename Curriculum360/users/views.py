from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



from .forms import UserAddForm
# Create your views here.
def register_user(request):
    form = UserAddForm()
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            messages.success(request , ("Succussfully Registerd !"))
            return redirect('dashboard')
    
    form = UserAddForm()
    
    return render (request, 'register_user.html' , {'form':form})
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Loged in success fully!'))
            return redirect('dashboard')
            
        else:
            messages.success(request, ('Login error, please try correct username or password!'))
            return render(request, 'login.html')
    else :
        return render(request, 'login.html')
