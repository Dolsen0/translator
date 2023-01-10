from translate import Translator
from text_to_speech import speak

#available languages:
#(en, ja, ko, pt, zh, zh-TW, etc)

translator = Translator(to_lang="pt")

message = input("\nWhat would you like to say? \n")
conversation = translator.translate(message)

print(conversation)
speak(message, "en", save=True, file="message_original.mp3", speak=True)
speak(conversation, "pt", save=True, file="message_translated.mp3", speak=True)

