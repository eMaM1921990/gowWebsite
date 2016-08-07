# -*- coding: utf-8 -*-

from django.core.mail import send_mail
from django import forms

__author__ = 'emam'


class ContactForm(forms.Form):
    typeChoices = [('الادارة', 'الادارة'),
                   ('المبيعات', 'المبيعات'),
                   ('التسويق', 'التسويق'),
                   ('الادارة القانونية', 'الادارة القانونية'),
                   ('قسم الاعلانات', 'قسم الاعلانات'),
                   ('قسم المندوبين', 'قسم المندوبين'),
                   (' الشكاوى و الاقتراحات', 'الشكاوى و الاقتراحات'),
    ]

    first_name = forms.CharField(max_length=30, label='First name',
                                 widget=forms.TextInput(attrs={'placeholder': 'First name','class':'form-control input-md'}), required=True)
    last_name = forms.CharField(max_length=30, label='Last name',
                                widget=forms.TextInput(attrs={'placeholder': 'Last name','class':'form-control input-md'}), required=True)
    email = forms.EmailField(max_length=30, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email','class':'form-control input-md'}),
                             required=True)
    department = forms.ChoiceField(choices=typeChoices, label='Department', widget=forms.Select(), required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def is_valid(self):
        if hasattr(self, 'cleaned_data'):
            if self.cleaned_data['first_name'] is None or len(self.cleaned_data['first_name']) == 0:
                return False
            if self.cleaned_data['last_name'] is None or len(self.cleaned_data['last_name']) == 0:
                return False
            if self.cleaned_data['email'] is None or len(self.cleaned_data['email']) == 0:
                return False
            if self.cleaned_data['department'] is None or len(self.cleaned_data['department']) == 0:
                return False
            if self.cleaned_data['content'] is None or len(self.cleaned_data['content']) == 0:
                return False

            return True

    def sendMail(self):
        if hasattr(self, 'cleaned_data'):
            message = 'Contact Name: ' + self.cleaned_data['first_name'] + self.cleaned_data['last_name'] + '\n'
            message += 'Email: ' + self.cleaned_data['email'] + '\n'
            message += 'Department: ' + self.cleaned_data['department'] + '\n'
            message += 'content: ' + self.cleaned_data['content']
            send_mail('Request From gate', message, settings.EMAIL_HOST_USER, [settings.EMAIL_TO],fail_silently=True)

