#importar librerias

import speech_recognition as sr
import os


#obtenemos ruta del archivo
ruta_proyecto = os.path.dirname(os.path.abspath(__file__))

#contruimos la ruta completa
ruta_audio = os.path.join(ruta_proyecto, "src", "mondongo meme shorts.wav")

#mostramos la ruta
print("buscando audio en :" , ruta_audio)

#inicianilizamos recorning osea reconoce la voz.

recognizer = sr.Recognizer()

with sr.AudioFile(ruta_audio) as source:
    audio = recognizer.record(source)


try:
    texto = recognizer.recognize_google(audio, language = "es-PE")
    print("transcripcion")
    print(texto)
except sr.UnknownValueError:
   print("no se pudo entender el audio") 
except sr.RequestError:
    print("error con el servicio")
finally:
    print("se ejecuto todo")


