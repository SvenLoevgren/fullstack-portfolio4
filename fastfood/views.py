from django.shortcuts import render


# Create your views here.
def first_testview(request):
    return render(request, 'fastfood/fastfood_home.html')