from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import Register


class SignUpView(generic.CreateView):
    form_class = UserCreationForm

    template_name = 'registration/signup.html'


def register(request):
    if request.method == 'POST':
        user_form = Register(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'pages/index.html', {'form': new_user})
    else:
        user_form = Register()
    return render(request, 'registration/signup.html', {'form': user_form})
