from modeltranslation.translator import translator, TranslationOptions
from .models import Blog

class BlogTranslationOptions(TranslationOptions):
	fields = ('blockName', 'LongBlockName', 'text')
	# empty_values = {'name': '', 'content': ''}
translator.register(Blog, BlogTranslationOptions)