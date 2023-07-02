from django.template.response import TemplateResponse
from django.shortcuts import render

def index(request):
    return TemplateResponse(
        request, 'contact/index.html', {
            'site_logo_name': 'mkdevs-logo',
            'site_name': 'mkdevs',
            'site_description': 'Let\'s brings your ideas and projects to life!',
            'page_title': 'Contact - mkdevs'
        }
    )

