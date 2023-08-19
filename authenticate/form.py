from django import forms
from django.contrib.auth.forms import UserCreationForm
from authenticate.models import UserCus

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({
        'type' : "username",
        'name' : "username",
        'required':''
        })

        self.fields['mail'].widget.attrs.update({
            'type': "email",
            'name': "email",
            'required': '',
        })

        self.fields['password1'].widget.attrs.update({
            'type': "password",
            'name': "password1",
            'required': '',
        })

        self.fields['password2'].widget.attrs.update({
            'type': "password",
            'name': "password2",
            'required': '',
        })
        self.fields['job'].widget.attrs.update({
            'type': "text",
            'name': "job",
            'required': '',
        })
        self.fields['image'].widget.attrs.update({
            "id":"image",
            "type":"file" ,
            "placeholder":"Avatar",
            "alt":"image_uplaod_avatar",
            "name":"images"
        })
    class Meta:
        model = UserCus
        fields = ['username', 'mail', 'password1','password2', 'job', 'image']


class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               max_length=500,
                               widget=forms.TextInput(attrs={
                                   'placeholder': "username",
                                   "type": "text",
                                   'required': "",
                                   "name": "username"
                               }))
    password = forms.CharField(label='', max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': "Mot de passe:",
                                   "type": "password",
                                   'id': "inputGroup-sizing-lg",
                                   "name": "password"
                               }))
