from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm, ProfileEditForm, UserEditForm
from .models import Profile
from django.contrib import messages



@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
	if request.method == 'POST':
		form = UserSignUpForm(data=request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			profile = Profile.objects.create(user=new_user)
			return render(request, 'account/sign_up_confirm.html', {'new_user': new_user})
	else:
		form = UserSignUpForm()
	return render(request, 'account/sign_up.html', {'form': form})


@login_required
def edit(request):
	if request.method == "POST":
		profile_form = ProfileEditForm(data=request.POST, instance=request.user, files=request.FILES)
		user_form = UserEditForm(data=request.POST, instance=request.user)
		if profile_form.is_valid() & user_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Profile updated successfully')
		else:
			messages.error(request, 'Error updating your profile')
	else:
		profile_form = ProfileEditForm(instance=request.user.profile)
		user_form = UserEditForm(instance=request.user)
	return render(request, 'account/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})


