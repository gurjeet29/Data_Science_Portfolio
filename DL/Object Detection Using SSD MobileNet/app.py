import os
from flask import Flask, request, redirect, render_template, flash
from werkzeug.utils import secure_filename
import cv2
import numpy as np


UPLOAD_FOLDER = 'static/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'
ALLOWED_EXTENSIONS = {'jpg', 'png', '.jpeg'}
app = Flask(__name__)


# APP CONFIGURATIONS
app.config['SECRET_KEY'] = 'opencv'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 10mb
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file attached in request')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            process_file(os.path.join(UPLOAD_FOLDER, filename), filename)
            data = {
                "processed_img": 'static/downloads/'+filename,
                "uploaded_img": 'static/uploads/'+filename
            }
            return render_template("index.html", data=data)
    return render_template('index.html')


def process_file(path, filename):
    detect_object(path, filename)


def detect_object(path, filename):

    class_labels = []
    file_name = 'coco.names'
    with open(file_name, 'rt') as fpt:
        class_labels = fpt.read().rstrip('\n').split('\n')

    config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weights = 'frozen_inference_graph.pb'
    thres = 0.5  # threshold to detect object
    nms_thres = 0.2  # lower value more suppression

    model = cv2.dnn_DetectionModel(weights, config_file)

    model.setInputSize(320, 320)
    model.setInputScale(1.0/127.5)
    model.setInputMean((127.5, 127.5, 127.5))
    model.setInputSwapRB(True)

    cap = cv2.imread(path)

    classindexs, confidence_interval, bbox = model.detect(
        cap, confThreshold=thres)

    # converting to list format for Non max supression
    bbox = list(bbox)
    confidence_interval = list(np.array(confidence_interval).reshape(1, -1)[0])
    confidence_interval = list(map(float, confidence_interval))

    indices = cv2.dnn.NMSBoxes(bbox, confidence_interval, thres, nms_thres)

    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]

        cv2.rectangle(cap, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.putText(cap, class_labels[classindexs[i][0]-1].upper(), (box[0]+10, box[1]+30),
                    cv2.FONT_HERSHEY_PLAIN, fontScale=2.7, color=(0, 255, 0), thickness=2)

        cv2.putText(cap, str(confidence_interval[i]*100), (box[0]+100, box[1]+30),
                    cv2.FONT_HERSHEY_PLAIN, fontScale=2.7, color=(0, 255, 0), thickness=2)

    cv2.imwrite(f"{DOWNLOAD_FOLDER}{filename}", cap)


if __name__ == '__main__':
    app.run(debug=True)
