from django.shortcuts import render
from django.http import HttpResponse
from .models import sitepages

# Create your views here.
def about(request):
    abouts = sitepages.objects.order_by('about_date')
    return render(request, 'sitepages/about.html', {'abouts':abouts})
