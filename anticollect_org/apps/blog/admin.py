from django.contrib import admin
from .models import Blog
from modeltranslation.admin import TranslationAdmin#,TranslationStackedInline

from django.forms import TextInput, Textarea
from django.db import models


class BlogAdmin(TranslationAdmin):
# class BlocksAdmin(admin.ModelAdmin):

    # list_display_links = ('id', 'title',)
    list_display = ['blockName', 'slug', 'idsort', 'image_tag', 'status',]
    list_editable = ['idsort', 'status']
    # ordering = ['slug', 'idsort',]
    sortable_field_name = "idsort"
    # list_filter = ('status', 'slug',)
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
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            # '/static/scripts/tiny-editor.js', # проверить
            '/static/modeltranslation/js/force_jquery.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(Blog, BlogAdmin)

# 'blockName', 'slug', 'idsort', 'banner', 'text', 'status',
#
#
#
# 'blockName'
# 'slug'
# 'created'
# 'lastmod'
# 'idsort'
# 'banner'
# 'text'
# 'status'