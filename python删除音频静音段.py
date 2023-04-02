import os
from pydub import AudioSegment
from pydub.silence import split_on_silence


def remove_silence(path1, path2):
    # os.walk函数 获得,目录下面的所有文件,,,,货区所有文件
    # 根目录,,,,文件夹,文件,,,,当然多个文件一定是存入一个容器里面,,,,一定是存入一个容器里面,,,,
    for root, dirs, files in os.walk(path1):
        # 对文件遍历,,,,
        for name in files:
            xx(os.path.join(root, name), name, path2)

# 这个函数叫做xx,还是使用pydub 传入文件名,,,,第一个是完整文件名,或者说文件夹和文件名的组合,,,,第三个又是什么路径呢?????
def xx(file1, name, path2):
    # 第一个文件名,,,得到sound这个文件流,,,,所有本地磁盘文件一定是用函数读取后做文件流的处理,,,做文件流的处理,,,,,,
    sound = AudioSegment.from_mp3(file1)
    #
    chunks = split_on_silence(sound,
                              # must be silent for at least half a second,沉默半秒
                              min_silence_len=600,
                              # consider it silent if quieter than -16 dBFS
                              silence_thresh=-27,
                              keep_silence=400
                              )
    sum = sound[:1]
    for i, chunk in enumerate(chunks):
        sum = sum + chunk
    #     输出为mp3格式,,,,
    sum.export(os.path.join(path2, name), format="mp3")
    print(name + "  已完成。")

# 这是批量操作 批量操作没有什么意思,必须界面可视化
remove_silence("语音训练数据集(个人录制)/0", "语音训练数据集(个人录制)/5")