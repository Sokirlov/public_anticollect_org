from django.db import models
from django.utils.translation import gettext as _
from index.models import Price
from django.contrib.auth.models import User

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

CHOISES_FROM= (
        ('site', 'Сайт'),
        ('viber', 'Viber'),
    )


def cur_user(request):
    loginNow = request.user
    return loginNow


class Clients(models.Model):
    CHOISES_PROCES=(
        ('no_worked', 'Новый Клиент'),
        ('payed', 'Оплачено'),
        ('in_court', 'Подано в Суд'),
        ('to_back', 'Возврат'),
    )
    CHOISES_ZAYAVKA=(
        ('new', 'Новая заявка'),
        ('later', 'Перзвонить Позже'),
        ('dogovor', 'Аванс'),
        ('refusal', 'Отказ'),
    )
    name = models.CharField(_('ПІБ'), max_length=300, null=True, blank=True)
    # tel = PhoneField(help_text='Контактний телефон', E164_only=False)
    tel = models.CharField('Телефон', max_length=20, help_text='Контактний телефон')
    summ = models.FloatField('Стягнута сума, грн *', null=True, blank=True)
    region = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.CASCADE, null=True, blank=True, default='')
    penalty = models.ForeignKey(Penalty, verbose_name='Взыскание',  on_delete=models.CASCADE, null=True, blank=True, default='')
    price = models.ForeignKey(Price, verbose_name='Тариф', on_delete=models.CASCADE, null=True, blank=True, default='')
    about = models.TextField('Описание', null=True, blank=True)
    dateAdd = models.DateTimeField('Дата создания', auto_now_add=True, help_text='Клиент создан', null=True, blank=True)
    lastModificate = models.DateTimeField('Последняя модификация', auto_now=True, help_text='последнее редактирование', null=True)
    processed = models.CharField('Статус клиента', choices=CHOISES_PROCES, max_length=20, blank=True, null=True, default='no_worked')
    pathFrom = models.CharField('Источник', choices=CHOISES_FROM, max_length=10, default='viber')
    datePayment = models.DateField('Дата по дог.', null=True, blank=True, auto_now=False)
    Payment = models.PositiveSmallIntegerField('Cумма по дог.', null=True, blank=True)
    operator = models.ForeignKey(User, verbose_name='Оператор', limit_choices_to={'groups__name': 'Operators'},
                                  null=True, blank=True, on_delete=models.SET_NULL)
    comments = models.TextField('Комментарии юриста', null=True, blank=True)
    manager = models.CharField('Статус заявки', choices=CHOISES_ZAYAVKA, max_length=15, blank=True, null=True, default='new')
    PrePayment = models.PositiveSmallIntegerField('Предоплата', null=True, blank=True)
    manager_comment = models.TextField('Комментарии менеджера', null=True, blank=True)



    class Meta:
        verbose_name = 'Заявка от клиента'
        verbose_name_plural = 'Заявки от клиентов'

    def __str__(self):
        return f'{self.tel}'