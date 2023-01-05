from django.shortcuts import render

# Create your views here.


def cdnfile(request):
    return render(request,'cdnfile.html')