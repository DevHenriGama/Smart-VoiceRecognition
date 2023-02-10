from vosk import Model, KaldiRecognizer
import speech_recognition as sr
import pyaudio
import json
import requests

model = Model('model')

rec = KaldiRecognizer(model,16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8000)
stream.start_stream()

def isOnlineMOde():
    _url = "www.google.com"
    try:
        _newRequest = requests.head(_url,timeout=3)
        return True
    except:
        return False


def OfflineRecognition():

    data = stream.read(4000)

    if rec.AcceptWaveform(data):
        Outvalue = json.loads(rec.Result())
        return  Outvalue['text']

def OnlineRecognition():

	sRec = sr.Recognizer()

	with sr.Microphone() as s:
		sRec.adjust_for_ambient_noise(s)

		while True:
			try:
				audio = sRec.listen(s)
				entrada = sRec.recognize_google(audio, language="pt_br")
				return entrada
			except sr.UnknownValueError:
				return ""



while True:
    if isOnlineMOde:
        print(OnlineRecognition())
    else:
        print(OfflineRecognition())
    

