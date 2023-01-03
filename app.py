from translate import Translator
from text_to_speech import speak

#available languages:
#(en, ja, ko, pt, zh, zh-TW, etc)

translator = Translator(to_lang="pt")
translation = translator.translate("very good, It's working")

message = input("\n What would you like to say? \n")
conversation = translator.translate(message)

speak(conversation, "pt", save=True, file="message.mp3", speak=True)


print(conversation)