from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



from .forms import UserAddForm
# Create your views here.
def register_user(request):
 
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = username
            
            user = form.cleaned_data.get("username")
            messages.success(request , ("Succussfully Registerd as " + user))
            return redirect('login')
        messages.success(request, ("Please check your form and try again \n Passwords must be similar and valid password,\n # 8 and more characters mixed with numbers is allowed"))
            
    else :
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
