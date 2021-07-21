from django.db import models
from django.utils.translation import gettext as _
from index.models import Price

class Penalty(models.Model):
    penalty = models.CharField('Завание удержания', max_length=50, null=True, blank=True)
    idsort = models.PositiveSmallIntegerField(verbose_name='Порядок сортировки', default=1)

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Взыскания'
        verbose_name_plural = 'Типы взысканий'

    def __str__(self):
        return self.penalty

class Region(models.Model):
    region = models.CharField('Регион', max_length=50, null=True, blank=True)
    idsort = models.PositiveSmallIntegerField(verbose_name='Порядок сортировки', default=1)

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.region


class Clients(models.Model):
    name = models.CharField(_('ПІБ'), max_length=300, null=True, blank=True)
    # tel = PhoneField(help_text='Контактний телефон', E164_only=False)
    tel = models.CharField('Телефон', max_length=20, help_text='Контактний телефон')
    summ = models.FloatField('Стягнута сума, грн *', null=True, blank=True)
    region = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.CASCADE, null=True, blank=True, default='')
    penalty = models.ForeignKey(Penalty, verbose_name='Взыскание',  on_delete=models.CASCADE, null=True, blank=True, default='')
    price = models.ForeignKey(Price, verbose_name='Тариф', on_delete=models.CASCADE, null=True, blank=True, default='')
    about = models.TextField('Описание', null=True, blank=True)
    dateAdd = models.DateTimeField('Дата создания', auto_now_add=True, help_text='Клиент создан', null=True, blank=True)
    lastModificate = models.DateTimeField('Дата последнего входа', auto_now=True, help_text='последнее редактирование', null=True)
    processed = models.BooleanField('Клиент обработан ?', null=True, default='False')

    class Meta:
        verbose_name = 'Заявка от клиента'
        verbose_name_plural = 'Заявки от клиентов'

    def __str__(self):
        return self.tel