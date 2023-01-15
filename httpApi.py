from flask import Flask, request, send_file
from lib.ImageBlur import ImageBlur
import os, random, string

class HttpApi:

    UPLOAD_FOLDER = './upload'
    ASSETS_FOLDER = './assets'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

    def __init__(self, imageBlur: ImageBlur) -> None:
        self.app = Flask(__name__)
        self.app.debug = False
        self.__imageBlur = imageBlur

        self.app.config['UPLOAD_FOLDER'] = HttpApi.UPLOAD_FOLDER
        self.app.config['MAX_CONTENT_LENGTH'] = 5 * 1000 * 1000
        self.app.add_url_rule('/', 'home', self.home)
        self.app.add_url_rule('/upload', 'upload', self.uploadFile, methods=["POST"])

    @staticmethod
    def allowed_file(filename: str):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in HttpApi.ALLOWED_EXTENSIONS

    def home(self):
        return send_file(os.path.join(HttpApi.ASSETS_FOLDER, 'index.html'))
    
    def uploadFile(self):
        if 'file' not in request.files:
            return 'No file in the request'
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return 'No file selected'
        if file and HttpApi.allowed_file(file.filename):
            print('Filename: ' + file.filename)
            ext = os.path.splitext(file.filename)[1]
            filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16)) + ext
            p = os.path.join(self.app.config['UPLOAD_FOLDER'], filename)
            # TODO use buffers to prevent doing a lot of IO operations
            file.save(p)
            self.__imageBlur.blurLicencePlate(p, p)
            return send_file(p)

    def start(self, port: int):
        self.app.run('0.0.0.0', port)
