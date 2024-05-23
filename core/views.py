from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.views import LogoutView


def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
        else:
            return render(request, 'core/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'core/signup.html', {'form': form})



class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # If the request method is GET, perform logout and redirect
        if request.method == 'GET':
            return self.get(request, *args, **kwargs)
        # For other methods, let the parent class handle it (POST)
        return super().dispatch(request, *args, **kwargs)
