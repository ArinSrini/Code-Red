import sys
import pyaudio
import wave
import time
import signal
import logging

CHUNK = 4096
FORMAT = pyaudio.paInt16
CHANNELS = 1  # Change to 1 for mono
LOOP_SECONDS = 2
RECORD_SECONDS = 6
WAVE_OUTPUT_FILENAME = "output2.wav"

p = pyaudio.PyAudio()
info = p.get_default_input_device_info()
RATE = int(info['defaultSampleRate'])

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

logging.info("* recording")

outfile = open(WAVE_OUTPUT_FILENAME, 'wb')
wf = wave.open(outfile, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)

def record():
    for i in range(0, RECORD_SECONDS // LOOP_SECONDS):
        for j in range(0, int(RATE / CHUNK * LOOP_SECONDS)):
            data = stream.read(CHUNK)
            wf.writeframes(data)

def cleanup():
    logging.info("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()
    outfile.close()

def handle_sigint(sig, frame):
    logging.info("Exiting!")
    cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

record()
cleanup()