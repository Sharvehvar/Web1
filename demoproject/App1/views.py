from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html')
def exhaust(request):
    return render(request, 'exhaust.html')
def ridinggears(request):
    return render(request, 'ridinggears.html')