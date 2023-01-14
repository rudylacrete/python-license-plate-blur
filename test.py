from lib.ImageBlur import ImageBlur

imgPath = '/home/rudy/Images/IMG_20210210_122842.jpg'
# imgPath = '/home/rudy/Images/photosFordNov21/drive-download-20211107T162813Z-001/DSC_0288.jpg'
imgBlur = ImageBlur()
imgBlur.blurLicencePlate(imgPath, 'test.jpg')
