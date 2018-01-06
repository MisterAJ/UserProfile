from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm,
                                        PasswordChangeForm)
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import AccountForm
from .models import Account


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('home')
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            user = authenticate(
                username=username,
                password=form.cleaned_data['password1']
            )
            account = Account()
            account.user = user
            account.first_name = username
            account.save()
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'accounts/sign_up.html', {'form': form})

@login_required
def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))

@login_required
def edit_profile(request, account_pk):
    account = get_object_or_404(Account, pk=account_pk)
    form = AccountForm(instance=account)
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            if request.user.is_authenticated():
                form.user = request.user
                form.save()
                return HttpResponseRedirect(
                    reverse('accounts:bio')
                )
            else:
                messages.error(
                    request,
                    "That user account has been disabled."
                )
        else:
            messages.error(
                request,
                "Form input is invalid."
            )
    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def bio(request):
    '''User Bio Page'''
    return render(request, 'accounts/bio.html')

@login_required
def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            old = form.cleaned_data['old_password']
            new = form.cleaned_data['new_password1']
            if old == new:
                messages.error(request, 'You can not use the same password.')
            else:
                form.save()
                messages.success(request, 'You have updated your password.')
                return HttpResponseRedirect(reverse('accounts:bio'))
    return render(request, 'accounts/password.html', {'form': form})
