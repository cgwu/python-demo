from django.db import models
from django import forms

# Create your models here.


# Validators && Forms.
def validate_comment_word_count(value):
    count = len(value.split()) # 单词的长度
    if count < 3:
        raise forms.ValidationError(('Please provide at least a 3 word message, %(count)s words is not descriptive enough'), params={'count': count},)

class ContactForm(forms.Form):
    name = forms.CharField(required=False, initial='Please provide your name')
    email = forms.EmailField(label='Your email', initial='We need your email')
    comment = forms.CharField(widget=forms.Textarea, validators=[validate_comment_word_count])

    # 验证单个field.
    def clean_name(self):
        value = self.cleaned_data['name']
        if value.isupper():
            raise forms.ValidationError("Please don't use all upper case for your name, use lowcase", code='uppercase')
        return value
    # 验证email.
    def clean_email(self):
        value = self.cleaned_data['email']
        if value.endswith('@hotmail.com'):
            raise forms.ValidationError("Please don't use a hotmail email, we simply don't like it", code='hotmail')
        return value

    def clean(self):
        # Call clean() method to ensure base class validation
        super(ContactForm,self).clean()
        name = self.cleaned_data.get('name','')
        email = self.cleaned_data.get('email','')
        # Check if the name is part of the email
        if name.lower() not in email:
            msg = "Please provide an email that contains your name, or viceversa"
            #raise forms.ValidationError(msg)
            self.add_error('name', msg)
            self.add_error('email', forms.ValidationError(msg))
            self.add_error(None, 'Form:' + msg)


