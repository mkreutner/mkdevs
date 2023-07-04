from datetime import datetime

from django.template.response import TemplateResponse
from django.views.decorators.csrf import requires_csrf_token
from django.conf import settings

from .models import ContactMessage

@requires_csrf_token
def index(request):
    if request.method.upper() == 'POST':
        cm = ContactMessage(
            name = request._post.get('name', None), 
            email = request._post.get('email', None), 
            message = request._post.get('message', None),
            created_date = datetime.now()
        )
        cm.save()

    c = {
        'settings': settings,
        'page_title': 'Contact - mkdevs'
    }
    
    return TemplateResponse(request, 'contact/index.html', c)

