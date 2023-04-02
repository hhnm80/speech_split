import os
import librosa
import pyloudnorm as pyln
import numpy as np
import soundfile as sf
import glob
import tqdm

sample_rate = 48000
trim_db = 30
# wav_db = -20.0

wav_db = -10.0


st_save_len = 150  # ms
end_save_len = 200  # ms

meter = pyln.Meter(sample_rate)


def process_wav(filename, file_o):
    wav, sr = librosa.load(filename, sr=sample_rate)
    loudness = meter.integrated_loudness(wav)
    wav = pyln.normalize.loudness(wav, loudness, wav_db)
    if np.abs(wav).max() > 1.0:
        wav = wav / np.abs(wav).max()

    wav = wav.astype(np.float32)
    cut_wav, index = librosa.effects.trim(
        wav,
        top_db=trim_db,
        frame_length=512,
        hop_length=128,
    )

    # index
    st_start, st_end = index[0], index[1]  # 这个可以用来进行手动调整静音长度,上面 cut_wav = wav[st_start, st_end]

    # new_s = max(st_start - int(st_save_len * sample_rate / 1000), 0)
    # new_d = min(st_end + int(end_save_len * sample_rate / 1000), len(wav))

    sf.write(file_o, cut_wav, sample_rate)

# 难道第一个参数是读取的文件全名,
process_wav("三 五 四 二 一 伯母 伯父.mp3","三 五 四 二 一 伯母 伯父_1.mp3")