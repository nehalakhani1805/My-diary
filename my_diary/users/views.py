from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
	if(request.method=="POST"):
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Welcome')
			return redirect('login')
	else:
		form=UserRegisterForm()
	return render(request,'users/register.html', {'form':form})
	
@login_required
def profile(request):
	if(request.method=="POST"):
		form=UserUpdateForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, f'Updated')
			return redirect('profile')
	else:
		form=UserUpdateForm(instance=request.user)
	return render(request,'users/profile.html', {'form':form})