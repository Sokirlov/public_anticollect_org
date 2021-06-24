from django.contrib import admin
from modeltranslation.admin import TranslationAdmin#,TranslationStackedInline
from .models import Blocks, Price, Contacts


class BlocksAdmin(TranslationAdmin):

    list_display_links = ('blockName', 'blcokId', 'slug',)
    list_display = ['blockName', 'blcokId', 'slug', 'idsort', 'hideTitle', 'status']
    list_editable = ['idsort', 'hideTitle', 'status']
    # ordering = ['slug', 'idsort',]
    sortable_field_name = "idsort"
    # list_filter = ('status', 'slug',)
    prepopulated_fields = {'slug': ('blcokId',)}

    fieldsets = (
        ('Разработано Sokolov for DG Finance',
         {'fields': ('blockName',  'blcokId', 'slug', ('status', 'hideTitle',), 'text'), }),
    )
    # readonly_fields = ('image_tag',)
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            # '/static/scripts/tiny-editor.js', # проверить
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(Blocks, BlocksAdmin)


class PriceAdmin(TranslationAdmin):

    list_display_links = ('name', 'price',)
    list_display = ['name', 'price', 'idsort', 'status']
    list_editable = ['idsort', 'status']
    # ordering = ['slug', 'idsort',]
    sortable_field_name = "idsort"
    # list_filter = ('status', 'slug',)
    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields': ('name','text', 'price', 'idsort', 'status'), }),
    )
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            # '/static/scripts/tiny-editor.js', # проверить
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(Price, PriceAdmin)

class ContactsAdmin(TranslationAdmin):

    list_display_links = ('name', 'tel', 'email',)
    list_display = ['name', 'tel', 'email', 'adress',  'code',]
    # list_editable = ['name', 'adress', 'code', 'tel', 'email']
    # ordering = ['idsort',]
    # sortable_field_name = "idsort"

    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields': ('name', 'adress', 'code', 'tel', 'email'), }),
    )
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            # '/static/scripts/tiny-editor.js', # проверить
            '/static/modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(Contacts, ContactsAdmin)


