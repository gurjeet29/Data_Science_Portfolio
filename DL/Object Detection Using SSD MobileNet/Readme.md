# Object Detection Using SSD-MobileNet

![image](https://user-images.githubusercontent.com/84326897/181575076-7ee8fefc-89c2-421e-b783-333b9a1195a8.png)

## Project Objective
The purpose of this project is to detect the objects using a webcam. Object detection is a computer technology related to computer vision and image processing that deals with detecting instances of semantic objects of a certain class (such as humans, buildings, or cars) in digital images and videos.

## Technologies
* Python
* OpenCV
* Pre-trained SSD MobileNet model

## Project Description
SSD (Single Shot MultiBox Detector) is a popular algorithm in object detection. It’s generally faster than Faster RCNN. I have implemented SSD MobilenetV2 trained over COCO dataset. You can detect any single class from the classes provided by COCO dataset.

The SSD architecture is a single convolution network that learns to predict bounding box locations and classify these locations in one pass. Hence, SSD can be trained end-to-end. The SSD network consists of base architecture (MobileNet in this case) followed by several convolution layers:

![img](https://user-images.githubusercontent.com/84326897/181575478-d1deb514-37a8-40c2-aca1-95a01d4c4436.png)

By using SSD, we only need to take one single shot to detect multiple objects within the image, while regional proposal network (RPN) based approaches such as R-CNN series that need two shots, one for generating region proposals, one for detecting the object of each proposal. Thus, SSD is much faster compared with two-shot RPN-based approaches.

## Testing
The model is tested using OpenCV where it detects the objects using our webcam.

**IF YOU FIND ANY ISSUES OR BUGS PLEASE OPEN AN ISSUE**
