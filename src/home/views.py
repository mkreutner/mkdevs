from django.template.response import TemplateResponse
from django.shortcuts import render
from django.conf import settings

def index(request):
    return TemplateResponse(
        request, 'home/index.html', {
            'settings': settings,
            'page_title': 'Home - mkdevs'
        }
    )

