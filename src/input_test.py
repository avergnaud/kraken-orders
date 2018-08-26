'''
https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries

(https://cloud.google.com/speech-to-text/docs/sync-recognize#speech-sync-recognize-python)

export GOOGLE_APPLICATION_CREDENTIALS="/home/...json

https://console.developers.google.com/apis/api/speech.googleapis.com/overview?project=...
'''

import pyaudio
import time
import io
import os

FORMAT = pyaudio.paInt16

CHANNELS = 1
RATE = 16000
CHUNK = int(RATE / 10)
RECORD_SECONDS = 5

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
            rate=RATE, input=True,
            frames_per_buffer=CHUNK)
print("recording (5 secondes)...")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("finished recording")


# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources',
    "audio_" + str(time.time()) + ".raw")

file = open(file_name, "wb")
file.write(b''.join(frames))
file.close()

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='fr-FR')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))

# ménage
os.remove(file_name)