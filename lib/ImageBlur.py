import yolov5
import cv2
import math

class ImageBlur:
    MIN_MODEL_CONF = 0.6 # minimum detection confidence
    def __init__(self) -> None:
        self.__model = yolov5.load('./model/best.pt')
        self.__model.conf = 0.25  # NMS confidence threshold
        self.__model.iou = 0.45  # NMS IoU threshold
        self.__model.agnostic = False  # NMS class-agnostic
        self.__model.multi_label = False  # NMS multiple labels per box
        self.__model.max_det = 20  # maximum number of detections per image

    def blurLicencePlate(self, srcPath: str, dstPath: str) -> None:
        results = self.__model(srcPath)
        predictions = results.pred[0]
        scores = predictions[:, 4]
        boxes = predictions[:, :4] # x1, y1, x2, y2
        
        image = cv2.imread(srcPath)

        for i in range(len(boxes)):
            # skip this detection if we are not sure this is a license plate
            if scores[i] < ImageBlur.MIN_MODEL_CONF:
                continue
            box = [math.floor(e) for e in boxes[i]]
            plate = image[box[1]:box[3], box[0]:box[2]]
            image[box[1]:box[3], box[0]:box[2]] = cv2.blur(plate, (55, 55))

        cv2.imwrite(dstPath, image)
