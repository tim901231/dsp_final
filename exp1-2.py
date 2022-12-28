from pydub import  AudioSegment
from pesq import pesq

source = "./clean_adjust_dB"
target = "./output/Enhanced/author/model370200/test/voicebank_Noisy_Test"

scores = []

for filename in os.listdir(source):

    f = os.path.join(source, filename)
    sound1 = AudioSegment.from_file(f).set_frame_rate(16000).get_array_of_samples()
    f = os.path.join(target, filename)
    sound2 = AudioSegment.from_file(f).set_frame_rate(16000).get_array_of_samples()

    sound1 = np.array(sound1)
    sound2 = np.array(sound2)
    score = pesq(16000, sound1, sound2, 'wb')
    scores.append(score)

print(sum(scores) / len(score))

    


