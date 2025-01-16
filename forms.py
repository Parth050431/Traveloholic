from django.forms import ModelForm
from django import forms

from .models import Contact


# class Usermessage(ModelForm):
# name = forms.CharField(required=True)
# email_id = forms.EmailField(required=True)
# subject = forms.CharField(required=True)
# message = forms.CharField(required=True)

# class Meta:
#     model = Contact
#     fields = ['name', 'email_id', 'subject', 'subject']


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {'message': forms.Textarea}
        # fields = ['name', 'email_id', 'subject', 'message']

    # name = forms.CharField(required=False)
    # email = forms.EmailField()
    # message = forms.CharField(max_length=1000)
