from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
# from index.models import Price
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from .models import Penalty, Region, Clients
from import_export.admin import ExportMixin
from django.contrib.auth.models import User
import datetime



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

# class ClientsAdmin(ImportExportModelAdmin):

def change_operator_to_op1(modeladmin, request, queryset):

    queryset.update(operator=User.objects.filter(groups__name='Operators')[0])
change_operator_to_op1.short_description = "Изменить оператора на op1"


def extract(n):
    return list(map(lambda x: x['name'], n))

# def time_formating():
#     return ClientsAdmin['dateAdd'].strftime("%d, %b %Y - %HH%Mm")


class ClientsAdmin(ExportMixin, admin.ModelAdmin):
    def get_fieldsets(self, request, obj=None):
        userGrops = extract(request.user.groups.all().values())
        if 'Operators' in userGrops:
            return (('Sokolov for DG Finance',
                     {'fields': ('name', 'tel', ('operator',), 'summ', 'price', 'about',)}),)
        elif 'Managers' in userGrops:
            return (('Sokolov for DG Finance',
                     {'fields': (('name', 'tel'), ('manager', 'PrePayment'), ('summ', 'price'), 'about', 'manager_comment',)}),)
        elif 'Lawyers' in userGrops:
            return (('Sokolov for DG Finance',
                     {'fields': (('name', 'tel'), ('summ', 'price', 'PrePayment',), 'datePayment', 'about', ('processed', 'Payment'),  'comments', )}),)
        else:
            return (('Разработано Sokolov for DG Finance',
                     {'fields': ('name', 'tel', ('processed', 'manager',), ('pathFrom', 'operator',),
                                 'comments', ('datePayment', 'Payment',),
                                 'lastModificate',
                                 ('summ', 'price',), 'about',
                                 )}),)

    def get_readonly_fields(self, request, *args, **kwargs):
        userGrops = extract(request.user.groups.all().values())
        if 'Managers' in userGrops:
            return ('tel',)
        elif 'Lawyers' in userGrops:
            return ('name', 'tel', 'summ', 'about', 'PrePayment',)
        else:
            return ('dateAdd', 'lastModificate',)

    def get_list_display(self, request):
        userGrops = extract(request.user.groups.all().values())
        if 'Operators' in userGrops:
            return ['tel', 'name', 'summ', 'price', 'about',]
        elif 'Managers' in userGrops:
            return ['name', 'tel', 'manager', 'summ', 'price','about', ]
        elif 'Lawyers' in userGrops:
            return ['name', 'tel', 'processed', 'summ', 'price', ]
        else:
            return ['id', 'dateAdd', 'lastModificate', 'pathFrom', 'operator', 'manager', 'processed', 'datePayment', 'Payment', 'comments', 'tel', 'name',  ]

    def get_list_filter(self, request):
        userGrops = extract(request.user.groups.all().values())
        if 'Operators' in userGrops:
            return (('dateAdd', DateRangeFilter))
        elif 'Managers' in userGrops:
            return (('lastModificate', DateRangeFilter), 'manager',)
        elif 'Lawyers' in userGrops:
            return (('lastModificate', DateRangeFilter), 'processed',)
        else:
            return ('pathFrom', 'manager', 'processed', ('dateAdd', DateRangeFilter), ('lastModificate', DateRangeFilter), ('datePayment', DateRangeFilter))

    # def get_actions(self, request):
    #     userGrops = extract(request.user.groups.all().values())
    #     if 'Operators' in userGrops or 'Managers' in userGrops or 'Lawyers' in userGrops:
    #         return None
    #
    #     return self

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        userGrops = extract(request.user.groups.all().values())
        if 'Operators' in userGrops:
            return qs.filter(operator=request.user, pathFrom='viber')
        elif 'Lawyers' in userGrops:
            return qs.filter(manager='dogovor')
        return qs

    def get_changeform_initial_data(self, request):
        get_data = super(ClientsAdmin, self).get_changeform_initial_data(request)
        get_data['operator'] = request.user.pk
        return get_data

    list_display_links = ('tel', 'name', 'processed', 'datePayment', 'Payment',)
    # list_display = ['tel', 'name',  'pathFrom', 'operator', 'processed', 'datePayment', 'Payment', 'comments', 'dateAdd', 'lastModificate', 'id']
    # list_editable = [ 'processed',]
    ordering = ['-dateAdd', ]
    list_filter = (('dateAdd', DateRangeFilter), 'pathFrom', 'processed', ('lastModificate', DateRangeFilter), ('datePayment', DateRangeFilter))# 'penalty', 'dateAdd',)
    search_fields = ('tel', "name",)
    list_per_page = 10
    list_max_show_all = 500
    # date_hierarchy = 'dateAdd'
    actions_on_bottom = True
    readonly_fields = ('dateAdd', 'lastModificate',)
    actions = [change_operator_to_op1]
    class Media:
            css = {
                'screen': (
                    '/static/css/admin_customs.css',
                )
            }
            js = (
                'https: // code.jquery.com / jquery-3.6.0.min.js'
                '/static/js/admin_clients.js',
            )
admin.site.register(Clients, ClientsAdmin)
