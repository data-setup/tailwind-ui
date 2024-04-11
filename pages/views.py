from django.shortcuts import render

# Home Page View
def home_view(request):
    return render(request, 'pages/home.html')

# About Page View
def about_view(request):
    return render(request, 'pages/about.html')
