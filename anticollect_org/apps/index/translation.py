from modeltranslation.translator import translator, TranslationOptions
from .models import Blocks, Price, Contacts

class BlocksTranslationOptions(TranslationOptions):
	fields = ('blockName', 'blcokId', 'text')
	# empty_values = {'name': '', 'content': ''}
translator.register(Blocks, BlocksTranslationOptions)

class PriceTranslationOptions(TranslationOptions):
	fields = ('name', 'text', )
	# empty_values = {'name': '', 'content': ''}
translator.register(Price, PriceTranslationOptions)

class ContactsTranslationOptions(TranslationOptions):
	fields = ('name', 'adress', )
	# empty_values = {'name': '', 'content': ''}
translator.register(Contacts, ContactsTranslationOptions)