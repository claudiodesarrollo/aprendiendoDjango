from django import forms
from django.core import validators


class FormArticle(forms.Form):
    title=forms.CharField(
        label="Titulo",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingresa un Titulo',
                'class':'titulo_form'
            }
        ),
        validators=[
            validators.MinLengthValidator(4,'El titulo es demasiado corto'),
            validators.RegexValidator('[^A-Za-z0-9]*$','El titulo es invalido','invalis title')
        ]
        
    )

    content=forms.CharField(
        label="Contenido",
        widget=forms.Textarea(
            attrs={
                'placeholder':'Ingresa unContenido',
                'class':'contenido_form'
            }
        )
    )

    public_options=[
        (1,'SI'),
        (0,'NO')
    ]

    public=forms.TypedChoiceField(
        label="Publicar",
        choices=public_options
    )