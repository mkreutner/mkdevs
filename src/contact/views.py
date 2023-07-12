from datetime import datetime

from django.template.response import TemplateResponse
from django.views.decorators.csrf import requires_csrf_token
from django.conf import settings

from .models import ContactMessage
from .forms import ContactMessageForm

@requires_csrf_token
def index(request):
    clean_form = True
    if request.method.upper() == 'POST':
        # Need to process the form data
        # - create a form instance and populate it with data from request
        form = ContactMessageForm(request.POST)
        # - check whether it's valid
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cm = ContactMessage(
                name = form.cleaned_data.get('name', None), 
                email = form.cleaned_data.get('email', None), 
                message = form.cleaned_data.get('message', None),
                created_date = datetime.now()
            )
            cm.save()
        else:
            clean_form = False
    
    # Create new form for next contact message
    if clean_form:
        form = ContactMessageForm()

    c = {
        'settings': settings,
        'page_title': 'Contact - mkdevs',
        'form': form
    }
    
    return TemplateResponse(request, 'contact/index.html', c)

