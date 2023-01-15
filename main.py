from lib.ImageBlur import ImageBlur
from httpApi import HttpApi

imgBlur = ImageBlur()

serv = HttpApi(imgBlur)
serv.start(8080)

# imgPath = '/home/rudy/Images/IMG_20210210_122855.jpg'
# imgPath = './upload/grmnuyqpzjivmsyx.jpg'
# imgPath = '/home/rudy/Images/photosFordNov21/drive-download-20211107T162813Z-001/DSC_0288.jpg'
# imgBlur.blurLicencePlate(imgPath, 'test.jpg')
