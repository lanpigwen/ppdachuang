from io import BytesIO
from synthesize import MYsynthesize
import os
import re

def sanitize_filename(filename):
    # 定义不允许出现在文件名中的符号
    invalid_chars = r'[\\/:"*?<>|]'

    # 使用正则表达式将不允许的符号替换为空格
    sanitized_filename = re.sub(invalid_chars, ' ', filename)
    
    return sanitized_filename

def wordtovoice(text,lan):
    """
    经过某函数，将输入的字段，转化为wav文件，并open with，返回一个file.read()
    """
    # 定义异步函数
    text=text.replace('?','？')
    text=sanitize_filename(text)
    MYsynthesize(text,lan)

    # # 创建协程并运行
    # asyncio.run(process_synthesis(text))

    file_name = text +'.wav'
    if lan=='zh':
        file_path = 'output/result/AISHELL3/' + file_name
    else:
        file_path = 'output/result/LJSpeech/' + file_name

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
    


