# Importing Python libraries

import speech_recognition as sr

rec = sr.Recognizer()

# Listening the audio
with sr.Microphone() as source:
    print('Say something.')
    audio = rec.listen(source)

# Trying to recognize the audio
try:
    print('JTRON thinks you said: ', rec.recognize_sphinx(audio))
except Exception as e:
    print('Error:  {0}'.format(e))




