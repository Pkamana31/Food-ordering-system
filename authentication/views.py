from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        # retrieve form data from post
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register') 

        # check if username is used
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken")
            return redirect('register') 

        # freate user and profile instance
        user = User.objects.create_user(username=username, password=password1, email=email)
        profile = Profile.objects.create(user=user, phone_number=phone_number, address=address)
        
        messages.success(request, "Registration successful. Please sign in.")
        # redirec
        return redirect('signin') 

    return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        # data from post
        username = request.POST.get('username')
        password = request.POST.get('password')

        # aut user
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # redirect
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'signin.html')

@login_required
def view_profile(request):
    profile = request.user.profile
    user = request.user
    orders = user.order_set.all()
    context = {
        'profile': profile,
        'orders': orders
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')
