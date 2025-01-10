from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import UserForm

# Create your views here.
def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def privacy_policy(request):
    return render(request, 'privacyPolicy.html')

def contacts(request):
    return render(request, 'contacts.html')

def tos(request):
    return render(request, 'tos.html')

from django.shortcuts import render, redirect
from .forms import UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('/')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserForm()
    return render(request, 'reg.html', {'form': form})