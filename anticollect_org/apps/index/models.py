from django.db import models
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError



class Banner(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    status = models.CharField('Состояние', max_length=20, choices=STATUS_CHOICES, default='draft',
                              help_text='можно скрыть блок, чтоб его не удалять.')
    title = models.CharField('Заголовок', max_length=250, null=True, blank=True)
    secondTitle = models.CharField('Заголовок2', max_length=50, null=True, blank=True)
    slug = models.SlugField('ID блока', blank=True, null=True,
                            help_text='техническое название блока должно быть из латинских букв и цифр')
    text = HTMLField('Текст сноски', blank=True, max_length=5000,
                     help_text='внутрення часть блока поддерживаються HTML теги')
    btn = models.CharField('Текст в кнопке', max_length=35, null=True, blank=True,
                           help_text='Максимальная длина текст, 35 символов с пробелами\nчтоб отключить оставить поле пустым')
    banner = models.ImageField('Картинка для фона', upload_to='bgr', null=True, blank=True,
                               help_text='минимальный размер 1280рх максимальный 2560рх по ширене\nдля белого фона оставить поле пустым')
    class Meta:
        verbose_name = 'Баннер (верхний блок)'
        verbose_name_plural = '1. Баннер (верхний блок)'

    def __str__(self):
        return self.title

class InfoOne(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    status = models.CharField('Состояние', max_length=20, choices=STATUS_CHOICES, default='draft',
                              help_text='можно скрыть блок, чтоб его не удалять.')
    title = models.CharField('Заголовок', max_length= 250, null=True, blank=True)
    slug = models.SlugField('ID блока', blank=True, null=True,
                            help_text='ID блока - идентификатор для ссылки в меню\nиспользовать только латинские буквы и цифры без пробелов')
    text = HTMLField('Текст сноски', blank=True, max_length=5000,
                     help_text='внутрення часть блока поддерживаються HTML теги')
    banner = models.ImageField('Картинка для фона', upload_to='banners', null=True, blank=True,
                               help_text='минимальный размер 1280рх максимальный 2560рх по ширене')
    class Meta:
        verbose_name = 'Инфо блок 1 '
        verbose_name_plural = '2. Инфо блок (второй блок под баннером)'

    def __str__(self):
        return self.title

class Services(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    status = models.CharField('Состояние', max_length=20, choices=STATUS_CHOICES, default='draft',
                              help_text='можно скрыть блок, чтоб его не удалять.')
    frontSide = HTMLField('Фронтальная сторона блока', max_length=500,  blank=True, null=True,
                     help_text='поддерживаються HTML теги')
    backSide = HTMLField('Тыльная сторона блока', max_length=500,  blank=True, null=True,
                     help_text='внутрення часть блока поддерживаються HTML теги')
    idsort = models.PositiveSmallIntegerField(verbose_name='Порядок сортировки', default=1)

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Блок услуг '
        verbose_name_plural = '3. Блок услуг'

    def __str__(self):
        return self.frontSide

class InfoTwo(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    status = models.CharField('Состояние', max_length=20, choices=STATUS_CHOICES, default='draft',
                              help_text='можно скрыть блок, чтоб его не удалять.')
    title = models.CharField('Заголовок', max_length=250, null=True, blank=True, )
    slug = models.SlugField('ID блока', blank=True, null=True,
                            help_text='ID блока - идентификатор для ссылки в меню\nиспользовать только латинские буквы и цифры без пробелов')
    textBefore = HTMLField('Текст сноски', blank=True, max_length=5000,
                     help_text='внутрення часть блока поддерживаються HTML теги')
    textAffter = HTMLField('Текст сноски', blank=True, max_length=5000,
                           help_text='внутрення часть блока поддерживаються HTML теги')
    btn = models.CharField('Текст в кнопке', max_length=35, blank=True, null=True,
                           help_text='Максимальная длина текст, 35 символов с пробелами\nчтоб отключить оставить поле пустым')

    class Meta:
        verbose_name = 'Инфо блок 2 '
        verbose_name_plural = '4. Инфо блок \n(между услугами и стадиями)'

    def __str__(self):
        return str(self.id)

class Stages(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    status = models.CharField('Состояние', max_length=20, choices=STATUS_CHOICES, default='draft',
                              help_text='можно скрыть блок, чтоб его не удалять.')
    title = models.CharField('Название этапа', max_length=500,
                     help_text='поддерживаються HTML теги')
    text = HTMLField('Описание этапа', max_length=500,  blank=True, null=True,
                     help_text='внутрення часть блока поддерживаються HTML теги')
    idsort = models.PositiveSmallIntegerField(verbose_name='Порядок сортировки', default=1)

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Блок стадий '
        verbose_name_plural = '5. Блок стадий'

    def __str__(self):
        return self.title

class Guarantees(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    status = models.CharField('Состояние', max_length=20, choices=STATUS_CHOICES, default='draft',
                              help_text='можно скрыть блок, чтоб его не удалять.')
    title = models.CharField('Гарантия', max_length=500,
                     help_text='поддерживаються HTML теги')
    text = HTMLField('Дополнительное описание', max_length=500,  blank=True, null=True,
                     help_text='внутрення часть блока поддерживаються HTML теги')
    idsort = models.PositiveSmallIntegerField(verbose_name='Порядок сортировки', default=1)

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Блок гарантии '
        verbose_name_plural = '7. Блок гарантии'

    def __str__(self):
        return self.title


class Price(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    name =models.CharField('Название пакета', max_length=200, null=True, blank=True)
    text = HTMLField('Описание пакета', blank=True, max_length=3000,
                     help_text='Опишите что входит в услугу')
    price = models.PositiveSmallIntegerField('Цена пакета')
    idsort = models.PositiveSmallIntegerField(verbose_name='Порядок сортировки', default=1)
    status = models.CharField('Состояние', max_length=20, choices=STATUS_CHOICES, default='draft',
                              help_text='можно скрыть блок, чтоб его не удалять.')
    stages =models.ManyToManyField(Stages, verbose_name='Выберети этапы', blank=True)
    remarq = models.CharField('Сноска со звездочкой', max_length=300, null=True, blank=True)


    class Meta:
        ordering = ['idsort']
        verbose_name = 'Цена'
        verbose_name_plural = '6. Цены'

    def __str__(self):
        return self.name

class Contacts(models.Model):
    name = models.CharField('Название', max_length=200, null=True, blank=True)
    adress = models.CharField('Адрес', max_length=200, null=True, blank=True)
    code = models.CharField('ЄДРПОУ', max_length=8, default=00000000)
    tel = models.CharField('Контактний телефон', max_length=20, blank=True, null=True)
    email = models.EmailField('e-mail')

    def save(self, *args, **kwargs):
        if Contacts.objects.count() < 2:
            super().save(*args, **kwargs)
        else:
            raise ValidationError('Слишком много записей')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = '8. Контакты'

    def __str__(self):
        return self.name

class TopMenu(models.Model):
    name = models.CharField('Название на кнопке', max_length=20, default='')
    link = models.CharField('Адрес ссылки', max_length=300, default='',
                           help_text='Для перемещения по блокам указать # и название указаное в ID блока\nнапример #price.')
    idsort = models.PositiveSmallIntegerField(verbose_name='Порядок сортировки', default=1)
    class Meta:
        verbose_name = 'Кнопки меню'
        verbose_name_plural = '0. Верхнее меню'

    def __str__(self):
        return self.name