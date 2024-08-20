from googletrans import Translator

text = input("enter your text : ")
lan = "bn"
translator = Translator()
translation = translator.translate(text,lan)
print(translation.text)
