from modeltranslation.translator import translator, TranslationOptions
from .models import Blog

class BlogTranslationOptions(TranslationOptions):
	fields = ('blockName', 'LongBlockName', 'text')
translator.register(Blog, BlogTranslationOptions)