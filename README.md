# dsp_final

## Experiment 1, Denoising with CDiffuSE

1. Clone the repository about CDiffuSE, install package
```
git clone https://github.com/neillu23/CDiffuSE.git
pip install -r requirements.txt
```

2. Put your noisy file into directory noisy_testset_wav
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

