from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
# from index.models import Price
from .models import Penalty, Region, Clients


class PenaltyAdmin(TranslationAdmin):
# class PenaltyAdmin(admin.ModelAdmin):
    list_display = ['penalty', 'idsort']
    list_editable = ['idsort',]
    sortable_field_name = "idsort"


    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields': ('penalty', 'idsort',), }),
    )


    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            # '/static/tiny_mce/tiny_mce.js',
            # '/static/tiny_mce/tiny_mce_init.js',
            # '/static/scripts/tiny-editor.js', # проверить
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
# class RegionAdmin(admin.ModelAdmin):
    list_display = ['region', 'idsort']
    list_editable = ['idsort',]
    sortable_field_name = "idsort"


    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields': ('region', 'idsort',), }),
    )

    class Media:
            js = (
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
                # '/static/tiny_mce/tiny_mce.js',
                # '/static/tiny_mce/tiny_mce_init.js',
                # '/static/scripts/tiny-editor.js', # проверить
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
    # sortable_field_name = "idsort"
    list_filter = ('processed', 'penalty', 'region', 'dateAdd',)
    search_fields = ("name",)
    # prepopulated_fields = {'slug': ('blcokId',)}

    fieldsets = (
        (
            'Разработано Sokolov for DG Finance', {
                'fields': ('name', 'tel', 'region', 'processed', 'lastModificate', 'summ', 'penalty', 'price', 'about',
                           ), }
        ),
    )
    readonly_fields = ('dateAdd', 'lastModificate',)
    # class Media:
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
    #         '/static/tiny_mce/tiny_mce.js',
    #         '/static/tiny_mce/tiny_mce_init.js',
    #         '/static/scripts/tiny-editor.js', # проверить
    #         '/static/modeltranslation/js/force_jquery.js',
    #         '/static/modeltranslation/js/tabbed_translation_fields.js',
    #     )
    #     css = {
    #         'screen': (
    #             '/static/modeltranslation/css/tabbed_translation_fields.css',
    #         ),
    #     }
admin.site.register(Clients, ClientsAdmin)



# 'name', 'tel', 'summ', 'region', 'penalty', 'price', 'about'