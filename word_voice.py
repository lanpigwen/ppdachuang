from io import BytesIO


def text_wav(text):
    """
    输入：text

    输出：example.wav文件地址、"example.wav"文件名

    根据text生成 example.wav文件，返回example.wav的文件地址
    """
    return "example.wav","example.wav"

def wordtovoice(text):
    """
    经过某函数，将输入的字段，转化为wav文件，并open with，返回一个file.read()
    """
    file_path,file_name=text_wav(text)

    if text == "示例文字":
        with open(file_path,'rb') as open_wav:
            data=open_wav.read()
            bytes_io = BytesIO(data)
        return bytes_io,file_name


