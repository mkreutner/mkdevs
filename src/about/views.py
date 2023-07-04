from django.template.response import TemplateResponse
from django.shortcuts import render
from django.conf import settings

def index(request):
    return TemplateResponse(
        request, 'about/index.html', {
            'settings': settings,
            'page_title': 'About - mkdevs'
        }
    )

