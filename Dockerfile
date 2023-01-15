FROM ultralytics/yolov5:v7.0-cpu

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

ADD . .

CMD python3 main.py
