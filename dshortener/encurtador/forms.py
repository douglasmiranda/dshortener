from django.forms import ModelForm, TextInput, URLField
from models import Link


class EncurtarURLForm(ModelForm):
    url = URLField(widget=TextInput(attrs={
        'placeholder': 'Entre com a URL que deseja encurtar...',
    }))
    class Meta:
        model = Link