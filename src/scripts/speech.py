# Importing Python libraries

import speech_recognition as sr

# Declared the recognizer
rec = sr.Recognizer()

# Listening the audio
with sr.Microphone() as source:
    print('zi ceva uai ci cu tini')
    audio = rec.listen(source)

# Trying to recognize the audio
try:
    print('JTRON thinks you said: ', rec.recognize_sphinx(audio))
except Exception as e:
    print('da vorbeste cuaimiu clar:  {0}'.format(e))




