# -*- coding: utf-8 -*-
# from datetime import datetime, time

from pydub import AudioSegment
from pydub.silence import detect_silence
import os
import uuid
import time


# 生成guid
def GUID():
    return str(uuid.uuid1()).replace("-", "")


# 分割文件
def SplitSound(filename, save_path, save_file_name, start_time, end_time, audio_type='mp3'):
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

def SplitSilence(file_name, save_path, audio_type='mp3'):
    sound = AudioSegment.from_file(file_name, format=audio_type)



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
            SplitSound(file_name, save_path, str(index) + ".mp3", start_point, end_point)
            index = index + 1
        start_point = item[1]

    # 处理最后一段音频
    # sound.len
    SplitSound(file_name, save_path, str(index) + ".mp3", start_point, len(sound))
    # len(sound)


audioPath = "C:/test/育才路15号广西师范大学育才校区 2(1).mp3"

# audioPath = "C:/test/育才路15号广西师范大学育才校区 6(1).mp3"
# audioPath = "C:/test/育才路15号广西师范大学育才校区 6(1).m4a"


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




# SplitSilence(audioPath, savePath)

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

# # 读取音频文件函数,,,
# import scipy.io.wavfile as wav
#
# fs, audio = wav.read(audioPath)  #读取采样频率和具体的数值
# print(audio)
