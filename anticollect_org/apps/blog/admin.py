from django.contrib import admin
from .models import Blog
from modeltranslation.admin import TranslationAdmin
from django.forms import TextInput, Textarea
from django.db import models


class BlogAdmin(TranslationAdmin):
    list_display = ['blockName', 'slug', 'idsort', 'image_tag', 'status',]
    list_editable = ['idsort', 'status']
    sortable_field_name = "idsort"
    prepopulated_fields = {'slug': ('blockName',)}

    fieldsets = (
        ('Кейс работ', {'fields':
                            ('blockName', 'slug', 'LongBlockName',
                                ('idsort', 'status',),
                             ('banner', 'image_tag',),
                             'metaDescrioption', 'metaKeyWords',
                             'text', 'lastmod',
                            ),
                        }),
    )
    readonly_fields = ('image_tag', 'created', 'lastmod',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '120'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 120})},
    }
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(Blog, BlogAdmin)