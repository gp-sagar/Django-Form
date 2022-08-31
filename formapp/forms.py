# import email
# from email import message
# from unittest.util import _MAX_LENGTH
from django import forms
import re

# Django Create Form

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     phone = forms.IntegerField(max_value=1000000000)
#     email = forms.EmailField(max_length=254)
#     message = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#         help_text='Write here your message!'
#     )
#     source = forms.CharField(       # A hidden input for internal use
#         max_length=50,              # tell from which page the user sent the message
#         widget=forms.HiddenInput()
#     )

#     def clean(self):
#         cleaned_data = super(ContactForm, self).clean()
#         name = cleaned_data.get('name')
#         email = cleaned_data.get('email')
#         phone = cleaned_data.get('Phone')
#         message = cleaned_data.get('message')
#         if not name and not email and not message:
#             raise forms.ValidationError('You have to write something!')

# Coustom Form using django
from django.core.validators import RegexValidator
validate_char = RegexValidator(
    regex = "[0-9]",
    message = "Enter a valid value."
)
        

class colorfulcontactform(forms.Form):
    name = forms.CharField(
        max_length=30,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Enter Your Name'
            }
        ),
        validators=([validate_char])
    )
    email = forms.EmailField(
        max_length = 40,
        widget = forms.EmailInput(),
        help_text = 'kbnvj  kfenb kvmna bkvjf enbj'
    )
    message = forms.CharField(
        max_length = 255,
        widget = forms.Textarea(),
        help_text = 'Elaborate Your Concern'
    )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('name')
    #     if re.match("[a-zA-Z]", name):
    #         raise forms.ValidationError('Only charectors allowed.')


    
