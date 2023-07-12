from django import forms
from captcha.fields import CaptchaTextInput

class ContactMessageForm(forms.Form):
    name = forms.CharField(
        required = True, 
        max_length = 512,
        widget = forms.TextInput()
    )
    email = forms.EmailField(
        required = True,
        widget = forms.EmailInput()
    )
    message = forms.CharField(
        required = True, 
        widget = forms.Textarea()
    )
    captcha = forms.CharField(
        required=True,
        widget = CaptchaTextInput()
    )    

