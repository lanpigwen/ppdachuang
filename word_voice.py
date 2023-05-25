from io import BytesIO
from synthesize import MYsynthesize
import os


def text_wav(text):
    """
    输入：text

    输出：example.wav文件地址、"example.wav"文件名

    根据text生成 example.wav文件，返回example.wav的文件地址

    """


    return "example.wav","example.wav"

# import asyncio

def wordtovoice(text):
    """
    经过某函数，将输入的字段，转化为wav文件，并open with，返回一个file.read()
    """
    # 定义异步函数
    # async def process_synthesis(text):
    MYsynthesize(text)

    # # 创建协程并运行
    # asyncio.run(process_synthesis(text))

    file_name = text +'.wav'
    file_path = 'output/result/AISHELL3/' + file_name

    try:
        with open(file_path, 'rb') as open_wav:
            data = open_wav.read()
            bytes_io = BytesIO(data)
        open_wav.close()
        os.remove(file_path) #删除wav
        os.remove(file_path[0:-4]+'.png') #删除png
        return bytes_io, file_name,'seccessed'
    except:
        with open('output/result/AISHELL3/语音生成失败，请您重新尝试！.wav', 'rb') as open_wav:
            data = open_wav.read()
            bytes_io = BytesIO(data)
        open_wav.close()
        return bytes_io, file_name,'failed'
    


