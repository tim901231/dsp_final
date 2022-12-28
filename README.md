# dsp_final

Recommend run in colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pmfr4qFPk1hDQNAVSr4JtLpKw4L-haut?usp=sharing)


## Experiment 1, Denoising with CDiffuSE

1. Clone the repository about CDiffuSE, install package
```
git clone https://github.com/neillu23/CDiffuSE.git
pip install -r requirements.txt
```

2. Put your noisy file into directory /noisy_testset_wav
the file need to be .wav, you can convert your voice with only converter

If you only have clean voice file, you can put your file into directory voice_mix, and type (not need to be .wav file)

```
python3 ./mix.py
```
it will generate noisy file with your voice and save file in noisy_test_wav

3. Setup the path, enter CDiffuSE and run inference.sh
```
./setup.py
cd CDiffuSE
./inference.sh 1 author 370200
```
4. Your result will in ./output/Enhanced/author/model370200/voiceban

5. For evaluation, see colab notebook ("we use testing dataset of DEMAND")


```
cd .. # at dsp_final
rm -r noisy_testset_wav
rm -r clean_adjust_dB
mkdir DEMAND
mkdir clean_adjust_dB
mkdir noisy_testset_wav
wget -O ./clean_test.zip https://datashare.ed.ac.uk/bitstream/handle/10283/2791/clean_testset_wav.zip?sequence=1&isAllowed=y
unzip -q ./clean_test.zip -d DEMAND
python3 exp1-1.py  # default: wind SNR=17.5dB
cd CDiffuSE
./inference.sh 1 author 370200
cd ..
python3 exp1-2.py

```
## Experiment 2

1. move the noisy file to matlab/mix/. The fil should be in wav format.

2. use either command
```
classical('./mix/', './out/')
```
in matlab GUI terminal, or 
```
matlab -nodisplay -r "classical('./mix/', './out/')"
```
in shell. The output wav will be in matlab/out.