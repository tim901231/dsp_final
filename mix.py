import os
from pydub import  AudioSegment


dir = 'voice_mix'
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    sound = AudioSegment.from_file(f)

    wind = AudioSegment.from_file('./noise/wind.wav')
    output = sound.overlay(wind, loop=True)
    output.export(f'./noisy_testset_wav/{filename.split(".")[0]}_wind.wav', format='wav')

    rain = AudioSegment.from_file('./noise/rain.mp3')
    output = sound.overlay(rain, loop=True)
    output.export(f'./noisy_testset_wav/{filename.split(".")[0]}_rain.wav', format='wav')
