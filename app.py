from translate import Translator
translator = Translator(to_lang="pt")
translation = translator.translate("very good, It's working")

print(translation)