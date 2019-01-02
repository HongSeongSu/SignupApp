from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth import get_user_model

from .forms import SignupForm, ProfileForm

User = get_user_model()


def main_view(request):
    if request.method == 'POST':
        return redirect(reverse('step1'))
    return render(request, 'member/default.html', {})


def step1view(request):
    if request.method == 'POST':
        return redirect(reverse('step2'))
    return render(request, 'member/step1.html')


def step2view(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)

        if signup_form.is_valid():
            signup_form.signup()
            n_user = authenticate(
                username=signup_form.cleaned_data['username'],
                password=signup_form.cleaned_data['password_confirm'],
            )
            login(request, n_user)
            return redirect(reverse('step3'))

    else:
        signup_form = SignupForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'member/step2.html', context)


@login_required
def step3view(request):
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(reverse('step4'))
    else:
        profile_form = ProfileForm(instance=request.user)

    context = {
        'profile_form': profile_form,
    }
    return render(request, 'member/step3.html', context)


def step4view(request):
    return render(request, 'member/step4.html')