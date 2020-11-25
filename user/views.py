from django.shortcuts import render

from .forms import UserRegistrationForm, ChangeUserForm


def create_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'user/register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'user/registration.html', {'user_form': user_form})


def change_user(request):
    user = request.user
    if request.method =='POST':
        user_form = ChangeUserForm(request.POST, instance=user)
        if user_form.is_valid():
            user.avatar_image = request.FILES.get('avatar_image')
            user_form.save()
    else:
        user_form = ChangeUserForm(instance=request.user)
    return render(request, 'user/change_user.html', {'user_form': user_form})
