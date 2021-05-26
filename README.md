# Shoe Detector
Repository for a shoe object detection model trained in Tensorflow 1.14 for the electric longboard

# Introduction
## Goals
After brainstorming ways that we could implement **machine learning** into our [electric longboard](https://github.com/mleblan67/Electric_longboard), we decided that a feature where the board could follow a user's shoes without the user having to pick up the board would be cool. I broke this problem down into three parts: use object detection to figure out where the shoes are from the camera attached to the longboard, figure out the shoe distance based on the size and position of the bounding boxes, and finally sending power to the motors to move the longboard in the required direction. I hoped that this would allow the longboard to follow a user walking away, and move away from a user walking towards it.
## Object Detection
![Object detection gif](https://ckhconsulting.com/wp-content/uploads/2020/11/object-detection.gif)

Object detection is a part of computer vision which is a huge field in deep learning. It allows computers identify objects in an image, and classify what that object is. As you can already see, the importance and implications of this are huge. This technology powers the self-driving car industry, and can vastly improve security and cameras.

Object detection is a field much bigger and more complex than I could even scratch the surface of this year. So, I focused my energy on training and understanding an [SSD MobilenetV2 model](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz). This model is made up of two parts:a MobilenetV2 base network, and an SSD multibox detector. MobilenetV2, like other base networks (Inception, Resnet), is a high level feature extruder and classifier that helps find the objects. However, MobilenetV2 is a much more lightweight and mobile network, which makes it optimal for running on a Raspberry pi. Next, SSD multibox detector is a detector that splits up the image into a grid, helps find the likelihood of an object at each point in the grid, and creates bounding boxes for each detection with location, name, and confidence. The low confidence boxes are then cut out, leaving us with a highly confident and accurate model. More information about [SSD](https://arxiv.org/abs/1512.02325) and [MobilenetV2](https://arxiv.org/abs/1801.04381) can be found in the linked papers.

# Training the model
## Collecting and labelling the image data
The first part to building my shoe detector was building a shoe dataset. I could've collected hundreds of different images of shoes and people wearing shoes from the internet, but that would've taken forever. Instead, I collected 8 videos of people walking, 3 from the internet and 5 that I recorded of myself and others walking around, and extracted images from those videos using opencv and [this script](https://github.com/mleblan67/shoe_detector/blob/master/shoe_dataset/image_extractor.py). I then used an image labelling program called [labelimg](https://github.com/tzutalin/labelImg) to draw bounding boxes around every shoe in every picture. This resulted in 571 images and 3,160 total labled shoes. This step was by far the most tedious and boring, but also the most important. Bad data leads to bad models, so I had to make sure my data was as clean and useful as possible. I then uploaded my images and annotations to an online program called [Roboflow](https://roboflow.com/). This program allowed me to augment some pictures for greater color diversity and size in my dataset. I then exported the [tfrecords](https://github.com/mleblan67/shoe_detector/tree/master/tf1_model_trainer/tf_records), the data file Tensorflow uses to train on, with 1,300 training images and 121 validation images (92/8 split).
## Finding the base model
The easiest way to build an object detection model is by using a pretrained model and training it on your custom dataset. Most models found in the [Tensorflow Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md) are trained on the [COCO dataset](https://cocodataset.org/#home) or the Imagenet dataset. I found and downloaded an SSD MobilenetV2 model trained on COCO in the Model Zoo. This gives me checkpoints for the model (which I will use for tranfer learning), a configuration file, the pretrained COCO weights, and a saved model version (the standard version for TF2).
## Training and exporting the model
By far the longest part of this process is actually training the model. This is very CPU or GPU 

# Running the model
# Conclusion
## What I would've done differently
## Problems and solutions (and dead-ends)
