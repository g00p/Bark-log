import copy
import pyaudio
import wave
from functions import *
import audioop
from collections import deque


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 3
BUFFER_SECONDS = 2
WAVE_OUTPUT_FILENAME = get_audio_file_name()

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,)

# original read from pyaudio demo
# print("[-] recording")
#
#
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
#     rms = audioop.rms(data, 2)
#     print(rms)
# print("[+] done recording")
# Create fast I/O buffer

# frames = []
d = deque(maxlen=int(RATE / CHUNK * BUFFER_SECONDS))

while True:
    data = stream.read(CHUNK)
    d.append(data)
    rms = audioop.rms(data, 2)
    print(rms)
    if rms > 3000:
        frames = list(d)
        while True:
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data_2 = stream.read(CHUNK)
                frames.append(data_2)
                rms_2 = audioop.rms(data_2, 2)
                print('*****' + str(rms_2))
                print('L----'+ str(len(frames)))
                if rms_2 > 3000:
                    break
            # wf = wave.open(get_audio_file_name(), 'wb')
            wf = wave.open(get_audio_file_name(), 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
            break

stream.stop_stream()
stream.close()
p.terminate()

# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()