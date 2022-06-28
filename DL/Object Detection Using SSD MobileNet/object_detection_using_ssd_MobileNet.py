import cv2
import numpy as np

# img=cv2.imread('image.jpg')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)  # width
cap.set(4, 480)  # height
cap.set(10, 30)  # brightness

config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weights = 'frozen_inference_graph.pb'
thres = 0.5  # threshold to detect object
nms_thres = 0.2  # lower value more suppression

model = cv2.dnn_DetectionModel(weights, config_file)

class_labels = []
file_name = 'coco.names'
with open(file_name, 'rt') as fpt:
    class_labels = fpt.read().rstrip('\n').split('\n')

model.setInputSize(320, 320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

while True:
    success, img = cap.read()
    classindexs, confidence_interval, bbox = model.detect(
        img, confThreshold=thres)

    # converting to list format for Non max supression
    bbox = list(bbox)
    confidence_interval = list(np.array(confidence_interval).reshape(1, -1)[0])
    confidence_interval = list(map(float, confidence_interval))

    indices = cv2.dnn.NMSBoxes(bbox, confidence_interval, thres, nms_thres)

    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.putText(img, class_labels[classindexs[i][0]-1].upper(), (box[0]+10, box[1]+30),
                    cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 255, 0), thickness=2)
                    
        cv2.putText(img, str(confidence_interval[i]*100), (box[0]+100, box[1]+30),
                    cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 255, 0), thickness=2)

    # if len(classindexs) != 0:
    #     for classind, conf, box in zip(classindexs.flatten(), confidence_interval.flatten(), bbox):
    #         cv2.rectangle(img, box, (255, 0, 0), 2)
    #         cv2.putText(img, class_labels[classind-1].upper(), (box[0]+10, box[1]+30),
    #                     font, fontScale=font_scale, color=(0, 255, 0), thickness=2)
    #         cv2.putText(img, str(round(conf*100,2)), (box[0]+200, box[1]+30),
    #                     font, fontScale=font_scale, color=(0, 255, 0), thickness=2)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
