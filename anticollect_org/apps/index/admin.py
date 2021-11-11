from django.contrib import admin
from modeltranslation.admin import TranslationAdmin#,TranslationStackedInline
from .models import Price, Contacts, Banner, InfoOne, Services, InfoTwo, Stages, Guarantees, TopMenu, Feedbacks


class BannerAdmin(TranslationAdmin):
    list_display_links = ("title", "slug",)
    list_display = ["title", "slug", "status"]
    list_editable = ["status"]
    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields': (
            "title", "secondTitle", "mideleText",
            ("slug",  "status",),
            "banner", "btn", "text",),
        }),
    )

    def has_add_permission(self, request):
        if(len(Banner.objects.all()) > 0):
            return False
        else:
            return True

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(Banner, BannerAdmin)

class InfoOneAdmin(TranslationAdmin):
    list_display_links = ("title", "slug",)
    list_display = ["title", "slug", "status"]
    list_editable = ["status"]
    prepopulated_fields = {"slug": ("title",),}
    fieldsets = (('Разработано Sokolov for DG Finance', {'fields': (
            "title", ("slug",  "status",), "banner", "text",), }),)

    def has_add_permission(self, request):
        if(len(InfoOne.objects.all()) > 0):
            return False
        else:
            return True

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(InfoOne, InfoOneAdmin)


class InfoTwoAdmin(TranslationAdmin):
    list_display_links = ("id", "title", "slug",)
    list_display = ["id", "title", "slug", "status"]
    list_editable = ["status"]
    prepopulated_fields = {"slug": ("title",), }
    fieldsets = (('Разработано Sokolov for DG Finance', {'fields': (
            "title", ("slug",  "status",), "textBefore", "btn", "textAffter",), }),)

    def has_add_permission(self, request):
        if(len(InfoTwo.objects.all()) > 0):
            return False
        else:
            return True

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(InfoTwo, InfoTwoAdmin)

class ServicesAdmin(TranslationAdmin):
    list_display_links = ("frontSide",)
    list_display = ["id", "frontSide", "status", "idsort",]
    list_editable = ["status", "idsort",]
    list_filter = ("status",)
    fieldsets = (('Разработано Sokolov for DG Finance', {'fields': (
            ("idsort",  "status",), "frontSide", "backSide",), }),)
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(Services, ServicesAdmin)

class StagesAdmin(TranslationAdmin):
    list_display_links = ("id", "title",)
    list_display = ["id", "title", "status", "idsort",]
    list_editable = ["status", "idsort",]
    list_filter = ("status",)
    fieldsets = (('Разработано Sokolov for DG Finance', {'fields': (
            "title", ("idsort",  "status",), "text", ), }),)
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/js/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(Stages, StagesAdmin)


class GuaranteesAdmin(TranslationAdmin):
    list_display_links = ("id", "title",)
    list_display = ["id", "title", "status", "idsort",]
    list_editable = ["status", "idsort",]
    list_filter = ("status",)
    fieldsets = (('Разработано Sokolov for DG Finance', {'fields': (
            "title", ("idsort",  "status",), "text", ), }),)
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(Guarantees, GuaranteesAdmin)



class PriceAdmin(TranslationAdmin):
    list_display_links = ('name', 'price',)
    list_display = ['name', 'price', 'idsort', 'status']
    list_editable = ['idsort', 'status']
    ordering = ['idsort',]
    sortable_field_name = "idsort"
    list_filter = ('status',)

    fieldsets = (
        ('Разработано Sokolov for DG Finance',{'fields': ('name', ('price', 'idsort', 'status'), 'textLinkToForm', 'stages', 'remarq', 'text',), }),
    )
    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            # '/static/scripts/tiny-editor.js', # проверить
            '/static/modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
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

    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields': ('name', 'adress', 'code', 'tel', 'email'), }),
    )

    def has_add_permission(self, request):
        allcontact = len(Contacts.objects.all())
        if(allcontact > 0):
            return False
        else:
            return True

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(Contacts, ContactsAdmin)

class TopMenuAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'link', 'idsort',]
    list_editable =['name', 'link', 'idsort',]
    ordering = ['idsort',]
    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields': ('name', 'link'),
                                                'description':('<div class="help"><p><strong>Перечень всех блоков:</strong></p><ul style="list-style:none;"><li>/#info-1</li><li>/#oskarzhennya-vikonavchogo-napisu</li><li>/#service</li><li>/#info-2</li><li>/#etapi</li><li>/#price</li><li>/#guarantee</li><li>/#contactForm</li></ul></div>'),}),
    )
    def has_add_permission(self, request):
        allcontact = len(Contacts.objects.all())
        if(allcontact > 5):
            return False
        else:
            return True

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }

admin.site.register(TopMenu, TopMenuAdmin)

class FeedbacksAdmin(TranslationAdmin):
    list_display_links = ('id', 'text',)
    list_display = ['id', 'status', 'idsort', 'text',]
    list_editable = [ 'status', 'idsort', ]
    fieldsets = (
        ('Разработано Sokolov for DG Finance', {'fields': ('status', 'idsort', 'text', ), }),
    )

    class Media:
        js = (
            '/static/tiny_mce/tiny_mce.js',
            '/static/tiny_mce/tiny_mce_init.js',
            '/static/modeltranslation/js/force_jquery.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.2/jquery-ui.min.js',
            '/static/modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                '/static/modeltranslation/css/tabbed_translation_fields.css',
            ),
        }
admin.site.register(Feedbacks, FeedbacksAdmin)