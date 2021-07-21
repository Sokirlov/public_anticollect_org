from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Penalty, Region, Clients


class PenaltyAdmin(TranslationAdmin):
    list_display = ['penalty', 'idsort']
    list_editable = ['idsort',]
    sortable_field_name = "idsort"


    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields': ('penalty', 'idsort',), }),
    )


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/force_jquery.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(Penalty, PenaltyAdmin)

class RegionAdmin(TranslationAdmin):
    list_display = ['region', 'idsort']
    list_editable = ['idsort',]
    sortable_field_name = "idsort"


    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields': ('region', 'idsort',), }),
    )

    class Media:
            js = (
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
                '/static/modeltranslation/js/force_jquery.js',
                '/static/modeltranslation/js/tabbed_translation_fields.js',
            )
            css = {
                'screen': (
                    '/static/modeltranslation/css/tabbed_translation_fields.css',
                ),
            }
admin.site.register(Region, RegionAdmin)

class ClientsAdmin(admin.ModelAdmin):
    list_display_links = ('name', 'tel', 'summ',)
    list_display = ['dateAdd', 'name', 'tel', 'summ', 'processed']
    list_editable = ['processed']
    ordering = ['-dateAdd', ]
    list_filter = ('processed', 'penalty', 'region', 'dateAdd',)
    search_fields = ("name",)

    fieldsets = (
        (
            'Разработано Sokolov for DG Finance', {
                'fields': ('name', 'tel', 'region', 'processed', 'lastModificate', 'summ', 'penalty', 'price', 'about',
                           ), }
        ),
    )
    readonly_fields = ('dateAdd', 'lastModificate',)
admin.site.register(Clients, ClientsAdmin)