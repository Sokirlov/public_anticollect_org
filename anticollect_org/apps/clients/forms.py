from django.core import validators
from django.core.validators import validate_email
from django import forms
from django.utils.translation import gettext_lazy as _
from clients.models import Clients
from index.models import Price
# from django.contrib.localflavor.br.forms import BRPhoneNumberField
# from input_mask.contrib.localflavor.br.widgets import BRPhoneNumberInput



class ClientsForm(forms.ModelForm):
    price = forms.ModelChoiceField(queryset=Price.objects.all(),
                                   label='',
                                   empty_label=_("Виберіть послугу"),
                                   widget=forms.Select(attrs={'class': 'form-control'}),
                                   )
    # tel = BRPhoneNumberField(widget=BRPhoneNumberInput),
    class Meta:
        model = Clients
        fields = ('name', 'tel', 'summ', 'region', 'penalty', 'price', 'about')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('ПІП'), 'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'placeholder': _('Телефон'), 'class': 'form-control'}),
            'summ': forms.NumberInput(attrs={'placeholder': _('Стягнута сума, грн *'), 'class': 'form-control'}),
            # 'pagelink': forms.Select(),
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
            'region':'выберет регион',
        }
        # empty_label = {
        #     'region': 'выберет регион',
        # }
        # help_texts = {
        #     'region': _('Выбирите регион'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }
        # default_validators = [
        #     validators.validate_email
        # ]
    # def __init__(self, *args, **kwargs):
    #     super(ZakazForm, self).__init__(*args, **kwargs)
    #     self.fields['pagelink'].queryset = Category.objects.all().values_list('slug', 'categoryName')

    # def __init__(self, *args, **kwargs):
    #     super(ChoiceForm, self).__init__(*args, **kwargs)
    #     self.fields['pagelink'] = ModelChoiceField(queryset=Category.objects.all()), empty_label = "Choose a countries",)
# 'name', 'tel', 'summ', 'region', 'penalty', 'price', 'about'