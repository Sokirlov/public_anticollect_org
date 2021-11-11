from django.core import validators
from django.core.validators import validate_email
from django import forms
from django.utils.translation import gettext_lazy as _
from clients.models import Clients, CHOISES_FROM
from index.models import Price


class ClientsForm(forms.ModelForm):
    price = forms.ModelChoiceField(queryset=Price.objects.all(),
                                   label='', required=False,
                                   empty_label=_("Виберіть послугу"),
                                   widget=forms.Select(attrs={'class': 'form-control'}),
                                   )
    pathFrom = 'site'
    operator = None
    class Meta:
        model = Clients
        fields = ('name', 'tel', 'summ', 'price', 'about', )
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('ПІБ'), 'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'placeholder': _('Телефон'), 'class': 'form-control'}),
            'summ': forms.NumberInput(attrs={'placeholder': _('Стягнута сума, грн *'), 'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'penalty': forms.Select(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'placeholder': _('Короткий опис ситуації'), 'class': 'form-control'}),
            # 'pathFrom': forms.Textarea(),
        }
        labels = {
            'name': '',
            'email': '',
            'tel': '',
            'comments': '',
            # 'region':_('выберет регион'),
        }
        # default_validators = [
        #     validators.validate_email
        # ]
