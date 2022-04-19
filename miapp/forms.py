from random import choices
from django import forms

class FormArticle(forms.Form):
    title = forms.CharField(
        label = "Titulo"
    )

    content = forms.CharField(
        label = "Contenido",
        widget= forms.Textarea 
    )

    public_options = [
        (1,'Si'),
        (0,'No')
    ]

    public = forms.TypedChoiceField(
        label = "Public?",
        choices = public_options
    )