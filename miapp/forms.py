from random import choices
from django import forms

class FormArticle(forms.Form):
    title = forms.CharField(
        label      = "Titulo",
        max_length = 40,
        required   = False,
        widget     = forms.TextInput(
            attrs = {
                'placeholder': 'Title',
                'class': 'form-control'
            } 
        ) 
    )

    content = forms.CharField(
        label = "Contenido",
        widget= forms.Textarea(
            attrs = {
                'placeholder': 'Leave a comment here',
                'class': 'form-control'
            } 
        )  
    )

    public_options = [
        (1,'Si'),
        (0,'No')
    ]

    public = forms.TypedChoiceField(
        label = "Public?",
        choices = public_options
    )