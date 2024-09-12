from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Project

# Create your views here.
def main(request):
    context = {"projects": Project.objects.all().order_by("-id")}
    return render(request, "website/index.html", context)

def resume(request):
    return render(request, "website/resume.html")

def bio(request):
    return render(request, "website/bio.html")