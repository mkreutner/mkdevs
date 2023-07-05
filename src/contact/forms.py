from django import forms
from simplemathcaptcha.widgets import MathCaptchaWidget

class ContactMessageForm(forms.Form):
    name = forms.CharField(
        required = True, 
        max_length = 512,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Name'
            }
        )
    )
    email = forms.EmailField(
        required = True,
        widget = forms.EmailInput(
            attrs = {
                'class':'form-control',
                'placeholder': 'Email'
            }
        )
    )
    message = forms.CharField(
        required = True, 
        widget = forms.Textarea(
            attrs = {
                'class':'form-control', 
                'placeholder': 'Message',
                'rows': '5'
            }
        )
    )
    captcha = forms.CharField(
        required = True,
        widget = MathCaptchaWidget(
            start_int = 1,
            end_int = 100,
            question_tmpl = "%(num1)i %(operator)s %(num2)i = ",
            question_class = "form-control"
        )
    )
