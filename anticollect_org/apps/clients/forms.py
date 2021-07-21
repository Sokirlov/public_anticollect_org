from django import forms
from django.utils.translation import gettext_lazy as _
from clients.models import Clients
from index.models import Price


class ClientsForm(forms.ModelForm):
    price = forms.ModelChoiceField(queryset=Price.objects.all(),
                                   label='', required=False,
                                   empty_label=_("Виберіть послугу"),
                                   widget=forms.Select(attrs={'class': 'form-control'}),
                                   )

    class Meta:
        model = Clients
        fields = ('name', 'tel', 'summ', 'region', 'penalty', 'price', 'about')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('ПІБ'), 'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'placeholder': _('Телефон'), 'class': 'form-control'}),
            'summ': forms.NumberInput(attrs={'placeholder': _('Стягнута сума, грн *'), 'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'penalty': forms.Select(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'placeholder': _('Короткий опис ситуації'), 'class': 'form-control'}),
            # 'comments': forms.Textarea(attrs={'placeholder': _('Опишите ваш заказ')}),

        }
        labels = {
            'name': '',
            'email': '',
            'tel': '',
            'comments': '',
            'region':_('выберет регион'),
        }