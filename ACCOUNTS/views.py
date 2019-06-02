from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView,TemplateView
from django.contrib.auth import login
from . import forms
from . import models

class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'

class CustomerSignUpView(CreateView):
    model = models.User
    form_class = forms.CustomerSignUpForm
    template_name = 'accounts/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class VendorSignUpView(CreateView):
    model = models.User
    form_class = forms.VendorSignUpForm
    template_name = 'accounts/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

@login_required
def profile(request):
    if request.method=='POST':
        u_form=forms.UserUpdateForm(request.POST,instance=request.user)
        p_form=forms.ProfileUpdateForm(data=request.POST,files=request.FILES,
                                       instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your profile has been updated !')
            return redirect('profile')
    else:
        u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'accounts/profile.html',context)

@login_required
def contact_us(request):
    form=forms.ContactForm()
    if request.method=='POST':
        form=forms.ContactForm(data=request.POST)
        if form.is_valid():
            form.author=request.user
            form.save()
    return render(request,'accounts/contact_us.html',{'form':form})