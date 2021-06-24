from modeltranslation.translator import translator, TranslationOptions
from .models import Penalty, Region

class PenaltyTranslationOptions(TranslationOptions):
	fields = ('penalty',)
	# empty_values = {'idsort': '',}
translator.register(Penalty, PenaltyTranslationOptions)

class RegionTranslationOptions(TranslationOptions):
	fields = ('region',)
	# empty_values = {'idsort': '', }
translator.register(Region, RegionTranslationOptions)