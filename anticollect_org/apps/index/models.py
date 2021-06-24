from django.db import models
from phone_field import PhoneField
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError
import datetime


class Blocks(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    blockName = models.CharField('Заголовок блока', max_length=300, default='', help_text='Название блока, заголовок')
    blcokId = models.CharField('Название ссылки для меню',  help_text='Текст ссылки для меню сверху. рекомендовано одним словом', max_length=300, blank=True, null=True)
    slug = models.SlugField('ID блока',  blank=True, null=True, help_text='техническое название блока должно быть из латинских букв и цифр')
    text = HTMLField('Наполнение блока', blank=True, max_length=3000, help_text='внутрення часть блока поддерживаються HTML теги')
    idsort = models.PositiveSmallIntegerField(verbose_name='Порядок сортировки', default=1)
    status = models.CharField('Состояние', max_length=20, choices=STATUS_CHOICES, default='draft', help_text='можно скрыть блок, чтоб его не удалять.')
    created = models.DateTimeField(auto_now_add=True, null=True)
    hideTitle = models.BooleanField('Отображать заголовк ?', default='True', help_text='Если активно, то заголовок показывается заголовок блока.\nСнять галочку – скрыть заголовок.')

    class Meta:
        ordering = ['id']
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    def __str__(self):
        return self.blockName

class Price(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    name =models.CharField('Название пакета', max_length=200, null=True, blank=True)
    text = HTMLField('Описание пакета', blank=True, max_length=500,
                     help_text='')
    price = models.PositiveSmallIntegerField('Цена пакета')
    idsort = models.PositiveSmallIntegerField(verbose_name='Порядок сортировки', default=1)
    status = models.CharField('Состояние', max_length=20, choices=STATUS_CHOICES, default='draft',
                              help_text='можно скрыть блок, чтоб его не удалять.')

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return self.name

class Contacts(models.Model):
    name = models.CharField('Название', max_length=200, null=True, blank=True)
    adress = models.CharField('Адрес', max_length=200, null=True, blank=True)
    code = models.CharField('ЄДРПОУ', max_length=8, default=00000000)
    tel = PhoneField(help_text='Контактний телефон')
    email = models.EmailField('e-mail')

    def save(self, *args, **kwargs):
        if Contacts.objects.count() < 2:
            super().save(*args, **kwargs)
        else:
            raise ValidationError('Слишком много записей')

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name