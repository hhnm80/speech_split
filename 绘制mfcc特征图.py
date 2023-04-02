import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import matplotlib
from scipy.fft import fft
import librosa
import librosa.display

matplotlib.rc("font",family='SimHei') # 显示中文
matplotlib.rcParams['axes.unicode_minus']=False # 显示符号
# filename = 'D:\\code\\code\\audio process\\test.wav'


# filename = "F:\\桂林方言相关语料\\宜州官话\\词汇\\0002月亮.wav"

filename = "F:\\语音识别数据库\\数据库\\data_thchs30\\data\\A11_51.wav"

fs,signal = wav.read(filename)
#
# plt.figure()
# plt.subplot(2,1,1)#第一个子图
# plt.specgram(signal[:,0],Fs=fs,scale_by_freq=True,sides='default')
# plt.colorbar()#format='%+2.0f dB'
#
# plt.subplot(2,1,2)#第二个子图
# plt.specgram(signal[:,1],Fs=fs,scale_by_freq=True,sides='default')#绘制语谱图
# plt.colorbar(format='%+2.0f dB')
#
# plt.savefig('test2.jpg')
#
# #绘制频谱图
# plt.figure()
# ft=fft(signal[:,0])#需要注意 只能对一个通道的数据进行操作
# magnitude=np.absolute(ft)#取相似度
# magnitude=magnitude[0:int(len(magnitude)/2)+1]
# f=np.linspace(0,fs,len(magnitude))
# plt.plot(f,magnitude)
#
# plt.figure()
#绘制MFCC scipy与librosa的读取数据机制不一样
signal,fs=librosa.load(filename,sr=44100)#sr为采样率，mono
print(signal.shape,type(signal),len(signal))
#(2, 10411757) <class 'numpy.ndarray'> 2
mfccs=librosa.feature.mfcc(y=signal,n_mfcc=13,sr=fs)
print(type(mfccs))
librosa.display.specshow(mfccs,sr=fs)
#绘制一阶mfcc
plt.figure()
delta_mfccs=librosa.feature.delta(mfccs)
print(type(delta_mfccs))
librosa.display.specshow(delta_mfccs,sr=fs)
#绘制二阶mfcc
plt.figure()
delta2_mfccs=librosa.feature.delta(mfccs,order=2)
librosa.display.specshow(delta2_mfccs,sr=fs)
print(type(delta2_mfccs))
#绘制39个维度的mfcc
plt.figure()
mfcc=np.concatenate((mfccs,delta_mfccs,delta2_mfccs))#里面有括号
librosa.display.specshow(mfcc,sr=fs)
plt.show()
plt.savefig('test3.jpg')
