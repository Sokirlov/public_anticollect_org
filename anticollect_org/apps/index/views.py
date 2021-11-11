from django.shortcuts import render
from .models import Price, Contacts, Banner, InfoOne, Services, InfoTwo, Stages, Guarantees, Feedbacks


def index(request):
    try:
        banner = Banner.objects.get(status='published')
    except:
        banner = ''
    infoone = InfoOne.objects.filter(status='published')
    services = Services.objects.filter(status='published')
    infotwo = InfoTwo.objects.filter(status='published')

    stages = Stages.objects.filter(status='published')
    price = Price.objects.filter(status='published')
    guarantees = Guarantees.objects.filter(status='published')
    feedbacks = Feedbacks.objects.filter(status='published')


    return render(request, 'index/idx.html', {
        'banner': banner,
        'infoone': infoone,
        'services': services,
        'infotwo': infotwo,
        'stages': stages,
        'price': price,
        'guarantees': guarantees,
        'feedbacks': feedbacks,
    })