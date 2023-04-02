# -*- coding: utf-8 -*-
# from datetime import datetime, time
import numpy as np
from pydub import AudioSegment
from pydub.silence import detect_silence
import os
import uuid
import time
import mfcc_1标准版 as mfcc_tf


# 创建一个列表,用于存储汉字
list=[]
list.append("零"),list.append("一");list.append("二");list.append("三");list.append("四");list.append("五");list.append("六");list.append("七");list.append("八");list.append("九");list.append("十")
# 我们可以尝试把这些写入数据库里面
i=0;



















# 生成guid
def GUID():
    return str(uuid.uuid1()).replace("-", "")


# 分割文件
def SplitSound(filename, save_path, save_file_name, start_time, end_time, audio_type='wav'):
    if not os.path.exists(save_path):
        try:
            os.mkdir(save_path)
        except Exception as e:
            # 这里是打印异常的,,,,,,打印异常
            print(e)

    sound = AudioSegment.from_file(filename, format=audio_type)
    result = sound[start_time:end_time]
    final_name = save_path
    if not savePath.endswith("/"):
        final_name = final_name + "/"
    final_name = final_name + save_file_name

    result.export(final_name, format=audio_type)
    # AudioSegment.export(result, format=audioType)
# 传入文件名,,,,还有保存的路径,我们再来看看怎么获取mfcc,,,,,,,怎么获取mfcc,有没有办法不存入文件里面,,,,,,

def SplitSilence(file_name, save_path, audio_type='wav'):
    sound = AudioSegment.from_file(file_name, format=audio_type)

    print("声音数据是:",sound)


    # print(len(sound))
    # print(sound.max_possible_amplitude)
    # start_end = detect_silence(sound,800,-57,1)
    start_end = detect_silence(sound, 300, -35, 1)

    # print(start_end)
    start_point = 0
    index = 1

    for item in start_end:
        if item[0] != 0:
            # 取空白部分的中位数
            end_point = (item[0] + item[1]) / 2

            # 注意这个print函数的作用,注意这个print函数的作用,,,,,,
            print("%d-%d" % (start_point, end_point))
            # 这个函数的作用是什么呢?????
            SplitSound(file_name, save_path, str(index) + ".wav", start_point, end_point)
            index = index + 1
        start_point = item[1]

    # 处理最后一段音频
    # sound.len
    SplitSound(file_name, save_path, str(index) + ".wav", start_point, len(sound))
    # len(sound)


audioPath = "C:/test/育才路15号广西师范大学育才校区 2(1).mp3"

audioPath = "C:/test/育才路15号广西师范大学育才校区 6(1).wav"


audioPath = "C:/test/五 九 八 六 七.wav"

savePath = "C://formatoutput/save"
# SplitSilence(audioPath, savePath)

# savePath重新组合,,,,构建一个路径,我们还需要文件名,,,,,切割文件名
# savePath=
file_name=audioPath.split("/")[-1]
# 输出育才路15号广西师范大学育才校区 2(1).mp3
print(file_name)
# 得到了文件名就好说了，，然后分割文件名的时候，我们做什么呢？？？就是把这些文件存入

# 但是我们还需要一个时间戳,不然的话遇到同名文件,这时候我们就gg了,,,
#

# savePath = "C://formatoutput/save"+"文件名"+"时间戳"

# print(time.strftime("%Y-%m-%d %H:%M:%S",local_time))
times = time.time()
local_time = time.localtime(times)
# 对时间格式化
date_time=time.strftime("%Y_%m_%d_%H_%M_%S",local_time)

# savePath = r"C:/formatoutput/save"+"/"+file_name+"_"+str(datetime.utcnow())
# 但是实际上,我们要去掉文件名的后缀,,,,
# file_name_without=file_name.split(".")[-1]



# savePath = "C:/formatoutput/save"+"/"+file_name+"_"+date_time
savePath = "C:/formatoutput/save"+"/"+file_name+"_"+date_time



# C://formatoutput/save/育才路15号广西师范大学育才校区 2(1).mp3/2023-03-28 08:42:18.561600
print(savePath)
# 这个文件夹就这么决定了么?????
# 没有这个文件夹怎么办,,,,
# 显然audioPath这是一个绝对路径,不能随便赋值,,,这个路径应该是我们获取
# 显然文件的绝对路径是存在的,,,,关键看保存路径
# 如果保存的路劲不存在,我们就创建这个文件夹,
if not (os.path.exists(savePath)):
    # 如果存在就执行操作
    # 创建文件夹
    os.makedirs(savePath)




SplitSilence(audioPath, savePath)

# 生成了文件以后,然后就是识别这些当文字,识别这些单个文字,,,,
# 得到了文件以后,就是搜索这里面的所有文件,,,,
# 



# 但是我们的目的是对切割后的语音单个字进行分类，，，，，所以我们并不需要把音频存储为文件，，，，我们只需要获得剪切后的文件流就可以，，，，


#         .....    是不是,,,,但是我发现切割后的文件流必须用专门的函数去处理,,,,,,,所以我们还是生成一个文件以后,我们直接去读取文件算了,,这样就需要我们去遍历那个文件夹.,,,,但是如果多次识别以后,,,,合格文件夹里面可能会存有很多东西,,,,,,所以我们需要识别以后删除文件夹里面的文件!!!!,对不对???????

# 但是这个文件夹,,比较固定,我们可不可以做点更进一步的事呢?????,我们可不可以按照文件的名字来生成保存文件夹呢,,,但是这种保存文件夹,我还是要识别以后再删除,,,,,
# 对savePath文件夹进行遍历,,,,,
# 读取savePath下面所有的文件,,,,,进行遍历,获取到了文件以后,我们就要读取文件名字
#
#

# files=os.listdir(savePath)
# print(type(files))
# print(files)
# for i in files:
#     # path=os.path.join('./T91_HR/'+i)
#     # print(path)
#     pass
# 这样把子文件夹里面的文件都获取了,,,但是我们不包括子文件夹,怎么不要搜索子文件夹里面的内容呢????,其实我们只要这么做

# 得到了一个语音的片段以后,,,

# 读取音频文件函数,,,
import scipy.io.wavfile as wav

fs, audio = wav.read(audioPath)  #读取采样频率和具体的数值
print(audio)

# 文件保存以后,还是搜索文件了,对保存文件夹进行文件搜索,

# import glob
#
# list = glob.glob("*.mp3")
# print(len(list))  # 输出文件个数

import os
from keras.models import load_model

# model = load_model("audio_lstm.h5")
#卷积
model = load_model("audio1.h5")


result=[]
for file_name in os.listdir(savePath):
    # 最后一段不处理,,,,最后一段是静音,不处理
    # 最后一段排除


    # 对每一个filename 这是相对文件名,我们要组成绝对文件名
    file_name=savePath+"/"+file_name
    print(file_name)

    # 读取文件,获得mfcc,,,,当然,我们可以搞一个
    # _mfcc_3 = mfcc_tf.get_mfcc_simplify(wav_file_1)
    mfcc = mfcc_tf.get_mfcc_simplify(file_name)

    #lstm模型
    # mfcc = np.array(mfcc).reshape(1, 32,40)
    # 卷积模型
    mfcc = np.array(mfcc).reshape(1, 32*40)



    # 填入的必须是一个向量,注意(32,40)和(1,32,40)的物理特性完全不一样,,,这在

    y_pre = model.predict(mfcc)
    print("预测结果是:", y_pre.shape)
    #
    print("预测结果是:", y_pre)
    #
    # # 返回的值用变量接受 就是把独热数组的下标提取出来了,看看是第几个项值最大
    real_pred = np.argmax(y_pre, axis=1)

    # real_pred是11个元素一维数组里面最大的一个元素的值,,,,这个值我们扔进去数据库取出汉字就可以了...,.

    # 我们预测了几个数字,,,,

    # real_pred是一个数组,这个数组只有一个元素,,,,
    # 这里的数值就是预测的值,从独热矩阵转换后的值
    print("real_pread的值是:",real_pred)
    # 预测值是: 爷爷

    # 或者说我们

    print("汉字预测值是:", list[real_pred[0]])

    result.append(list[real_pred[0]]+" ")


    # 调用模型预测,,,,

# 打印出最终结果
print("最终句子是:",result)