from django.db import models
# from phone_field import PhoneField
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
    # REGION_CHOICES = (
    #     ('Dnepropetrovsk', _('Дніпропетровська область')),
    #     ('Donetsk', _('Донецька область')),
    #     ('Zhytomyr', _('Житомирська область')),
    #     ('Transcarpathian', _('Закарпатська область')),
    #     ('Zaporozhye', _('Запорізька область')),
    #     ('Ivano-Frankivsk', _('Івано-Франківська область')),
    #     ('Kyiv and Kyiv', _('Київ та Київська область')),
    #     ('Kirovograd', _('Кіровоградська область')),
    #     ('Luhansk', _('Луганська область')),
    #     ('Lviv', _('Львівська область')),
    #     ('Mykolayivska', _('Миколаївська область')),
    #     ('Odessa', _('Одеська область')),
    #     ('Poltava', _('Полтавська область')),
    #     ('Rivne', _('Рівненська область')),
    #     ('Sevastopol', _('Севастополь')),
    #     ('Sumy', _('Сумська область')),
    #     ('Ternopil', _('Тернопільська область')),
    #     ('Kharkiv', _('Харківська область')),
    #     ('Kherson', _('Херсонська область')),
    #     ('Khmelnytsky', _('Хмельницька область')),
    #     ('Cherkasy', _('Черкаська область')),
    #     ('Chernivtsi', _('Чернівецька область')),
    #     ('Chernihiv', _('Чернігівська область')),
    # )
    name = models.CharField(_('ПІБ'), max_length=300, default='')
    # tel = PhoneField(help_text='Контактний телефон', E164_only=False)
    tel = models.CharField('Телефон', max_length=20, help_text='Контактний телефон')
    summ = models.FloatField('Стягнута сума, грн *')
    region = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.CASCADE)
    penalty = models.ForeignKey(Penalty, verbose_name='Взыскание',  on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    about = models.TextField('Описание', )
    dateAdd = models.DateTimeField('Дата создания', auto_now_add=True, help_text='Клиент создан', null=True, blank=True)
    lastModificate = models.DateTimeField('Дата последнего входа', auto_now=True, help_text='последний вход', null=True, blank=True)
    processed = models.BooleanField('Клиент обработан ?', null=True, default='False')

    class Meta:
        verbose_name = 'Заявка от клиента'
        verbose_name_plural = 'Заявки от клиентов'

    def __str__(self):
        return self.name