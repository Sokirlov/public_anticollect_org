from modeltranslation.translator import translator, TranslationOptions
from .models import Penalty, Region

class PenaltyTranslationOptions(TranslationOptions):
	fields = ('penalty',)
translator.register(Penalty, PenaltyTranslationOptions)

class RegionTranslationOptions(TranslationOptions):
	fields = ('region',)
translator.register(Region, RegionTranslationOptions)