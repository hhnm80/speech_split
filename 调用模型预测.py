import tensorflow
from keras.utils import to_categorical
from keras import models, layers
from keras.optimizers import RMSprop
from keras.datasets import mnist
from keras.models import load_model
import mfcc_1标准版 as mfcc_tf
import 数据库操作 as db_operator
import numpy as np
# 创建一个列表,用于存储汉字
list=[]
list.append("零"),list.append("一");list.append("二");list.append("三");list.append("四");list.append("五");list.append("六");list.append("七");list.append("八");list.append("九");list.append("十")
# 我们可以尝试把这些写入数据库里面
i=0;





# 在模型预测这里,虽然我们分出了要识别的数字是哪一类,但是我们需要转换为汉字,我尝试过汉字作为训练标签,但是不知道为什么不行,所以建立一套数据库系统,,,,

# 首先我们要创建相关的数据库
# db_operator.crete_dateBase_speech_recognition()
# # 创建了数据库以后,我们就连接这个数据库,,,,,
# db_operator.connect_db()

## 其实插入数据库是实现自动化操作,就是我们自动把类别数字和汉字对应填入数据表中,但是实际上,如果我们手动设计了数据表,就不需要实现这一步的自动化操作,只需要事先手动设计数据库,然后得到了数字的分类后,在数据库里面查询出汉字就可以了.....这么做的原因是我们事先知道这个数据库是什么样子,我们知道要插入什么数据,假设我们要构建一个网站,上线发布给用户使用,用户要提交什么数据我们也不知道,因此这时候我们就需要使用数据库插入函数,,,,,因为这时候,数据表最后的形式是什么样的,并不是我们自己所能预料的,这时候主动权只能


# 卷积网络模型
model = load_model("audio1.h5")


# model = load_model("audio_lstm.h5")



# 首先获取一个文件的mfcc值,
# wav_file = "H:\\语音识别数据库\\数据库\\data_thchs30\\data\\A11_51.wav"
# wav_file = "H:\\语音识别数据库\\伯父 (2).wav"

# wav_file = "伯父 (2).wav"

# wav_file = "伯父 (2).wav"

wav_file = "2 (2).wav"

wav_file = "4.wav"





# 再来一个音频文件,
# wav_file = "H:\\语音识别数据库\\5 (3).wav"

# wav_file = "H:\\语音识别数据库\\5 (3).wav"
# wav_file_1 = "H:\\语音识别数据库\\7月28日下午7点55分.wav"


# wav_file = "H:\\语音识别数据库\\3 (5).wav"

# _mfcc_3 = mfcc_tf.get_mfcc_simplify(wav_file_1)
mfcc = mfcc_tf.get_mfcc_simplify(wav_file)

#卷积
mfcc=np.array(mfcc).reshape(1,32*40)


# lstm
# mfcc=np.array(mfcc).reshape(1,32,40)

# (1, 532, 40)
print("删去第一维之前的形状",mfcc.shape)

# print(_mfcc)


# 先删去mfcc第一维
# _mfcc = np.array([np.squeeze(_mfcc, axis=0)])
# _mfcc_2 = np.squeeze(_mfcc_2)
# _mfcc_3 = np.squeeze(_mfcc_3)

# print("删去第一个维度后",_mfcc_2.shape)
# 对mfcc展开成一维数组
# _mfcc_2=_mfcc_2.reshape(32*40)
# _mfcc_3=_mfcc_3.reshape(32*40)


# 这么做的目的,看来我们必须传入一个二维数组,,,,一维数组也可以扩展为二维数组啊,我怎么忘了,比如(32,)可以变成(1,32),,,,增加一个维度,但是元素总数不变
# print("展开mfcc后的形状:",_mfcc.shape)

# 将需要测试的mfcc放入一个数组中
# mfcc=np.zeros((2,32*40))
# mfcc[0]=_mfcc_2
# mfcc[1]=_mfcc_3

# 填入的必须是一个向量,注意(32,40)和(1,32,40)的物理特性完全不一样,,,这在

y_pre=model.predict(mfcc)
print("预测结果是:",y_pre.shape)
#
print("预测结果是:",y_pre)
#
# # 返回的值用变量接受 就是把独热数组的下标提取出来了,看看是第几个项值最大
real_pred=np.argmax(y_pre,axis=1)

# real_pred是11个元素一维数组里面最大的一个元素的值,,,,这个值我们扔进去数据库取出汉字就可以了...,.

# 我们预测了几个数字,,,,


# real_pred是一个数组,这个数组只有一个元素,,,,
# 这里的数值就是预测的值,从独热矩阵转换后的值
print(real_pred)
#预测值是: 爷爷

# 或者说我们

print("预测值是:",list[real_pred[0]])

# 调用模型预测,,,,