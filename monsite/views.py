from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm
from .models import Client, Article, TrainingProgram

def index(request):
    return render(request, 'monsite/index.html')

def services(request):
    return render(request, 'monsite/services.html')

def contacts(request):
    return render(request, 'monsite/contact_form.html')

def clients(request):
    return render(request, 'monsite/clients.html')

def blog(request):
    tag = request.GET.get('tag')
    if tag:
        articles = Article.objects.filter(tag__icontains=tag)
    else:
        articles = Article.objects.all()
    articles = Article.objects.order_by('-date_publication')  # Affiche les articles les plus récents en premier
    return render(request, 'monsite/blog.html', {'articles': articles, 'selected_tag': tag})

def offer_detail(request, offre):
    return render(request, 'monsite/offer_detail.html', {'offre': offre})

def contact_form(request, offre):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('monsite:index')
    else:
        form = ContactForm()
    return render(request, 'monsite/contact_form.html', {'form': form, 'offre': offre})

def messages_list(request):
    messages = Client.objects.all().order_by('-date_created')
    return render(request, 'monsite/messages_list.html', {'messages': messages})

def download_program(request):
    program = get_object_or_404(TrainingProgram, id=1)  # Assurez-vous de récupérer le bon objet
    response = HttpResponse(program.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{program.filename}"'
    return response