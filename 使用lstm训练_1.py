from keras.datasets import mnist
#加载数据
from tensorflow import keras

import librosa
from glob import glob
import tensorflow as tf
from keras.layers import *
from keras.models import Sequential,load_model
from keras.utils.np_utils import to_categorical
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mfcc_1标准版 as mfcc_tf


# 为什么不准
#时间序列数量
n_step = 32
#每次输入的维度
n_input = 40

nbatch_size =3
nEpoches = 200

# 我们要训练的数据是mfcc,所以,我们需要先获取要训练的mfcc值,所以下面的函数就是用于获取训练参数
def tf_datasets(path):
  wav_file = glob(path+"/*/*.wav")
  #print (wav_file)
  # wav_file_len代表的是总音频文件数目,,,,
  wav_file_len = len(wav_file)
  x_train = np.zeros((wav_file_len,32,40))
  y_train = np.zeros((wav_file_len))
  # y_train=y_train.astype(str)
  # y_train = y_train.astype(np.str_)  # 转换成字符类型

  # 创建一个wav_file_len长度的列表,,,,,

  # y_train = ["" for i in range(wav_file_len)]



  for index,file in enumerate(wav_file):
      file_feature = mfcc_tf.get_mfcc_simplify(file)
      file_label = file.split("\\")[-2]
      x_train[index] = file_feature
      y_train[index] = file_label
      print (file_feature.shape,file_label)

  #       # 训练数据形状是: (257, 32, 40) (257,)  257是文件夹下面的音频文件的条数,或者说是有多少个音频文件,,,,
  return x_train,y_train


import numpy as np


# 分类类别数目
num_classes = 11
# 先获得训练的mfcc信息和标签信息....
path1 = "F:\\语音训练数据集(个人录制)"
x_train, y_train = tf_datasets(path1)
# 注意独热编码
y_train = to_categorical(y_train, num_classes)

# expected input data shape: (batch_size, timesteps, data_dim)
model = Sequential()
model.add(LSTM(32, return_sequences=True, input_shape=(n_step, n_input)))
model.add(LSTM(32, return_sequences=True))
model.add(LSTM(32))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
print(model.summary())


model.fit(x_train, y_train, batch_size=nbatch_size, epochs=nEpoches)
model.save("audio_lstm.h5")