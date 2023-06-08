'''This is file will contain methods used for translating text'''

from deep_translator import MyMemoryTranslator

# This is a function that will take in an english string input and translate to french
def english_to_french(english_text):

    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)

    return french_text


# This is a function that will take in a french string input and translate to english
def french_to_english(french_text):

    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)

    return english_text
    