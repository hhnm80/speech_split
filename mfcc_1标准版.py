#coding=utf-8
import tensorflow as tf
from tensorflow.python.ops import gen_audio_ops as audio_ops
from tensorflow.python.ops import io_ops
import numpy as np

# 这些是使用tensorflow自带的获取MFCC的方法
# sample_rate是每一秒的采样率
sample_rate, window_size_ms, window_stride_ms = 16000, 60, 30
dct_coefficient_count = 40
clip_duration_ms = 1000
second_time = 16  # 刚才测过了，这里最大的长度不超过16秒
# desired_samples = int(sample_rate * second_time * clip_duration_ms / 1000)
desired_samples = int(sample_rate * clip_duration_ms / 1000)




window_size_samples = int(sample_rate * window_size_ms / 1000)
window_stride_samples = int(sample_rate * window_stride_ms / 1000)


# (1, 332, 40)
# 这个相对于下面的simple来说，没有在audio_ops.decode_wav函数中设置desired_samples参数，但是经过我测试，可以通过设置desired_samples值对其进行补全和截断，
# 也就是说desired_samples的意思是期望的每个语音信号的时间长度
def get_mfcc_simplify_no_desired_samples(wav_filename, window_size_samples, window_stride_samples,
                                         dct_coefficient_count, max_length=160000):
    # 这里的max_length = 160000可以当做时间长短，一秒为16000帧，那么可以设置 时间 乘以 16000
    wav_loader = io_ops.read_file(wav_filename)
    wav_decoder = audio_ops.decode_wav(wav_loader, desired_channels=1)
    # print(wav_decoder) #这里是输出audio的长度，每一秒有16000字节，那么获取到的总的长度为 16000 * t

    # "这里需要说明，这里的每个文件，一秒钟的长度为16000帧，所以需要对长度进行设定"
    # 【因为训练文件全部是1秒钟长度，16000帧的，所以这里需要把每个语音文件的长度处理成一样的】
    audio = ((wav_decoder.audio))

    # 这里原本是设置对audio的长度进行处理，长的截断，短的补0,但是加上以后和下面带有desired_samples的函数一样
    # if len(audio) >= max_length:
    #     audio = audio[:max_length]
    # else:
    #     audio = tf.concat((audio, tf.reshape([0.] * (max_length - len(audio)), [-1, 1])), axis=0)

    # Run the spectrogram and MFCC ops to get a 2D 'fingerprint' of the audio.
    spectrogram = audio_ops.audio_spectrogram(audio, window_size=window_size_samples, stride=window_stride_samples,
                                              magnitude_squared=True)

    mfcc_ = audio_ops.mfcc(
        spectrogram,
        wav_decoder.sample_rate,
        dct_coefficient_count=dct_coefficient_count)  # dct_coefficient_count=model_settings['fingerprint_width']

    return mfcc_


def get_mfcc_simplify(wav_filename, desired_samples=desired_samples, window_size_samples=window_size_samples,
                      window_stride_samples=window_stride_samples, dct_coefficient_count=dct_coefficient_count):
    wav_loader = io_ops.read_file(wav_filename)
    wav_decoder = audio_ops.decode_wav(
        wav_loader, desired_channels=1, desired_samples=desired_samples)

    # Run the spectrogram and MFCC ops to get a 2D 'fingerprint' of the audio.
    spectrogram = audio_ops.audio_spectrogram(
        wav_decoder.audio,
        window_size=window_size_samples,
        stride=window_stride_samples,
        magnitude_squared=True)

    mfcc_ = audio_ops.mfcc(
        spectrogram,
        wav_decoder.sample_rate,
        dct_coefficient_count=dct_coefficient_count)  # dct_coefficient_count=model_settings['fingerprint_width']

    return mfcc_


import scipy.io.wavfile as wav
from python_speech_features import mfcc
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from keras.preprocessing.sequence import pad_sequences


# 对音频文件提取mfcc特征,这个计算出的结果和上面差不多，就是没有三行取一行，这里除以三以后，数值差不多
def compute_mfcc(file, numcep=dct_coefficient_count):
    fs, audio = wav.read(file)  # 读取采样频率和具体的数值
    mfcc_feat = mfcc(audio, samplerate=fs, numcep=numcep)  # 提取mfcc特征，出来的是一个矩阵，比如（910,26）
    mfcc_feat = mfcc_feat[::3]  # 对采样后的矩阵，每三行取一行数（304,26）
    # mfcc_feat = np.transpose(mfcc_feat)  #对矩阵进行转置，（26,304）
    # 对矩阵进行padding,在304行之后补0，最后补到500行，矩阵维度为（500,26）
    # mfcc_feat = pad_sequences(mfcc_feat, maxlen=500, dtype='float', padding='post', truncating='post').T
    return mfcc_feat

# 在这里调用mfcc函数,,,,,.,











if __name__ == "__main__":
    # wav_file = "H:\\语音识别数据库\\数据库\\data_thchs30\\data\\A11_51.wav"
    wav_file = "A11_51.wav"

    # wav_file = "9.wav"
    # wav_file = "call.wav"
    # wav_file = "Online.wav"


    # _mfcc = get_mfcc_simplify_no_desired_samples(wav_file, window_size_samples, window_stride_samples,dct_coefficient_count)
    #
    # # (1, 245, 40)
    # print(_mfcc.shape)

    # mfcc_feat = compute_mfcc(wav_file)
    #
    # print(mfcc_feat)
    # # (246, 26)
    # print(mfcc_feat.shape)

    _mfcc = get_mfcc_simplify(wav_file)
    # (1, 532, 40)
    print("删去第一维之前的形状",_mfcc.shape)

    # print(_mfcc)


    import matplotlib.pyplot as plt
    # 先删去mfcc第一维
    # _mfcc = np.array([np.squeeze(_mfcc, axis=0)])
    _mfcc = np.squeeze(_mfcc)

    print("删去第一个维度后",_mfcc.shape)

    # plt.imshow(_mfcc)

    plt.plot(_mfcc)
    plt.show()
    #((32, 40)

    print(_mfcc.shape)