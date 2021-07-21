from modeltranslation.translator import translator, TranslationOptions
from .models import Price, Contacts, Banner, InfoOne, Services, InfoTwo, Stages, Guarantees, TopMenu


class BannerTranslationOptions(TranslationOptions):
	fields = ("btn", "text", "title", "secondTitle",)
translator.register(Banner, BannerTranslationOptions)

class InfoOneTranslationOptions(TranslationOptions):
	fields = ("text", "title", )
translator.register(InfoOne, InfoOneTranslationOptions)

class ServicesTranslationOptions(TranslationOptions):
	fields = ("frontSide", "backSide", )
translator.register(Services, ServicesTranslationOptions)

class InfoTwoTranslationOptions(TranslationOptions):
	fields = ("title", "textBefore", "textAffter", "btn",)
translator.register(InfoTwo, InfoTwoTranslationOptions)

class StagesTranslationOptions(TranslationOptions):
	fields = ("text", "title", )
translator.register(Stages, StagesTranslationOptions)

class GuaranteesTranslationOptions(TranslationOptions):
	fields = ("text", "title", )
translator.register(Guarantees, GuaranteesTranslationOptions)





class PriceTranslationOptions(TranslationOptions):
	fields = ('name', 'text', 'remarq',)
translator.register(Price, PriceTranslationOptions)

class ContactsTranslationOptions(TranslationOptions):
	fields = ('name', 'adress', )
translator.register(Contacts, ContactsTranslationOptions)

class TopMenuTranslationOptions(TranslationOptions):
	fields = ('name',)
translator.register(TopMenu, TopMenuTranslationOptions)