from random import choices
from django import forms
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(
        label      = "Titulo",
        max_length = 40,
        required   = True,
        widget     = forms.TextInput(
            attrs = {
                'placeholder': 'Title',
                'class': 'form-control'
            } 
        ),
        validators=[
            validators.MinLengthValidator(4, 'The title is too short.'),
            validators.RegexValidator('^[A-Za-z0-9 ]*$', 'The title has wrong caracters')
        ] 
    )

    content = forms.CharField(
        label = "Contenido",
        widget= forms.Textarea(
            attrs = {
                'placeholder': 'Leave a comment here',
                'class': 'form-control'
            } 
        ),
        validators=[
            validators.MaxValueValidator('40', 'The content has a lot of words.')
        ]  
    )

    public_options = [
        (1,'Si'),
        (0,'No')
    ]

    public = forms.TypedChoiceField(
        label = "Public?",
        choices = public_options
    )