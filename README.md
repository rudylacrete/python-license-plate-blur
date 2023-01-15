This project is using a trained ML model built using Yolo. It can be found [here](https://huggingface.co/keremberke/yolov5m-license-plate)

OpenCv is then used to blur the area detected by the model.

# TODO

Some type of license plate is not detected correctly. The model need to be trained on extra images:
- black plates
- square plates (not rectangular)
