# Shoe Detector
Repository for a shoe object detection model trained in Tensorflow 1.14 for the electric longboard

# Introduction
## Goals
After brainstorming ways that we could implement **machine learning** into our [electric longboard](https://github.com/mleblan67/Electric_longboard), we decided that a feature where the board could follow a user's shoes without the user having to pick up the board would be cool. I broke this problem down into three parts: use object detection to figure out where the shoes are from the camera attached to the longboard, figure out the shoe distance based on the size and position of the bounding boxes, and finally sending power to the motors to move the longboard in the required direction. I hoped that this would allow the longboard to follow a user walking away, and move away from a user walking towards it.
## Object Detection
![Object detection gif](https://ckhconsulting.com/wp-content/uploads/2020/11/object-detection.gif)

Object detection is a part of computer vision which is a huge field in deep learning. It allows computers identify objects in an image, and classify what that object is. As you can already see, the importance and implications of this are huge. This technology powers the self-driving car industry, and can vastly improve security and cameras.

Object detection is a field much bigger and more complex than I could even scratch the surface of this year. So, I focused my energy on training and understanding an [SSD MobilenetV2 model](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz). This model is made up of two parts:a MobilenetV2 base network, and an SSD multibox detector. MobilenetV2, like other base networks (Inception, Resnet), is a high level feature extruder and classifier that helps find the objects. However, MobilenetV2 is a much more lightweight and mobile network, which makes it optimal for running on a Raspberry pi. Next, SSD multibox detector is a detector that splits up the image into a grid, helps find the likelihood of an object at each point in the grid, and creates bounding boxes for each detection with location, name, and confidence. The low confidence boxes are then cut out, leaving us with a highly confidetn and accurate model. More information about [SSD](https://arxiv.org/abs/1512.02325) and [MobilenetV2](https://arxiv.org/abs/1801.04381) can be found in the linked papers.

# Training the model
# Running the model
# Conclusion
## What I would've done differently
## Problems and solutions (and dead-ends)
