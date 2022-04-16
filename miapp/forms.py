from django import forms

class FormArticle(forms.form):
    title = forms.CharField(
        label = 'Titulo',
    )

    content = forms.CharField(
        label = "Contenido",
        widget= forms.Textarea 
    )