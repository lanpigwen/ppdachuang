from flask import Flask, request, Response,render_template,send_file
from word_voice import wordtovoice

app = Flask(__name__)



@app.route('/', methods=['POST','GET'])
def index():
    return render_template('bootstrap.html')


@app.route('/generate_voice', methods=['POST'])
def generate_voice():

    text = request.form['text']
    language=request.form['lan']
    print(language)
    #
    #
    bytes_io,file_name,state=wordtovoice(text,language)
    #
    #
    if state=='seccessed':
        return send_file(
            bytes_io,
            mimetype='audio/wav',
            as_attachment=True,
            download_name=file_name
        )
    else:
         return send_file(
            bytes_io,
            mimetype='audio/wav',
            as_attachment=True,
            download_name=file_name
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)



"""
    #holy shit...用wave.open读，怎么读都会跳过44字节的文件头，所以导致前端拿到的文件是不完整的！！！
    # with wave.open('magic.wav','rb') as wav_file:

    #     nframes = wav_file.getnframes()
    #     # print(nframes)
    #     wav_bytes = wav_file.readframes(nframes)
    #     print(wav_bytes[0:20])
    #     bytes_io = BytesIO(wav_bytes)
    #     bytes_io.seek(0)

    # with open('test.txt', 'rb') as f:
    #     bytes_io = BytesIO(f.read())
"""

"""
# @app.route('/file')
# def getfile():

#     return send_file(
#         'voice.wav',
#         mimetype='audio/wav',
#         attachment_filename='voice.wav'
#     )

"""