from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProfilePictureForm, SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            UserProfile.objects.create(user=user)

            login(request, user)

            return redirect("home_page")
    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', {'form': form})




@login_required
def profile_view(request):
    userdata=request.user
    return render(request,"profile.html",{'userdata':userdata})

@login_required
def update_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  
    else:
        form = ProfilePictureForm(instance=request.user.userprofile)

    return render(request, 'update_profile_picture.html', {'form': form})