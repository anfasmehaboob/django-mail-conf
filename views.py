from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    projects = Projects.objects.order_by('-id')
    context = {
        'projects': projects
    }
    return render(request,'index.html',context)

def project_detail(request,pk_id):
    projects = Projects.objects.get(id=pk_id)
    context = {
        'projects':projects
    }
    return render(request,'project_detail.html',context)



def projects(request):
    projects = Projects.objects.order_by('-id')
    context = {
        'projects':projects
    }
    return render(request,'projects.html',context)


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        return render(request,'mail.html')
    return render(request,'contact.html')
