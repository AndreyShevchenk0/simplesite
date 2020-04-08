#from django.shortcuts import render  # бил тут етот код
from django.http import HttpResponse
from django.template import loader

from.models import Bb


def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
    # s = 'Список обьявлений\r\n\r\n\r\n'
    # for bb in Bb.objects.order_by('-published'):
    #     s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    # return HttpResponse(s, content_type='text/plain; charset=utf-8')
    #return HttpResponse('<h1>Здесь будет список обьявлений!</h1>')
