import os
from pydub import  AudioSegment


def set_loudness(sound, target_dBFS):
    loudness_difference = target_dBFS - sound.dBFS
    return sound.apply_gain(loudness_difference)

dir = 'voice_mix'
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    sound = AudioSegment.from_file(f)

    wind = AudioSegment.from_file('./noise/wind.wav')
    wind = set_loudness(wind, target_dBFS=-30)
    output = sound.overlay(wind, loop=True)
    output.export(f'./noisy_testset_wav/{filename.split(".")[0]}_wind.wav', format='wav')

    rain = AudioSegment.from_file('./noise/rain.mp3')
    rain = set_loudness(rain, target_dBFS=-30)
    output = sound.overlay(rain, loop=True)
    output.export(f'./noisy_testset_wav/{filename.split(".")[0]}_rain.wav', format='wav')
