# Ball-Launcher-Reinforcement-Learning
This project consists on designing, assembling and coding a ball tossing robot that learns how to play basketball. The robot uses an IP camera to capture images, and then learns how to throw the ball by means of Reinforcement Learning. For more information, please read the uploaded PDF document **Implementation of a tossing ball robot using**

You can see the video of the final prototype in [here](https://vimeo.com/670613697)

## Design
Solidworks files can be obtained from the folder 'SolidWork parts'

## 3D Print
The .stl documents can be found in the folder 'Print STL files'. I used the printers Zortrax M200 and Zmorph VX.

![ASSEMBLY](images/ASSEMBLY.PNG)

## Assembly and Electronics
Electronic scheme
![ELECTRICAL_DIAGRAM](images/ELECTRIC_DIAGRAM.PNG)

## Communicatrion protocols
This part of the project consists on sending the learned actions from the RL model to the robot. To do this, a UDP protocol has been used to send data from the Python server to the ESP8266 Wi-Fi client. The robot’s controller (the ESP8266 board) receives this data and maps the actions into feasible outputs to control the motors and the servo.
You can test the communication with the following 2 files:
- **UDP_ESP8266.ino**: The ESP8266 board receives data packets from Python via the UDP protocol
- **udp_socket.py**: A test script that sends the desired information from Python to the ESP8266 board

## Computer Vision
We have managed to extract images from an [IP Camera](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US&gl=US).
The file **main_Computer_Vision.py** contains the necessary functions to extract some features from a red object, to be used as states in the RL environment.
This file does the following:
- Obtain the frames from an IP Camera
- Segment the frames to extract just the red colors
- Apply an opening to eliminate blobs generated by a bad red segmentation
- Extract the corners from the detected red object
- Plot a rectangle on top of the image frames containing the red object
- Plot the position of the centroid, and the width and height of the object

## Reinforcement Learning
Finally, the entire Reinforcement Learning scripts and all the necessary explanations can be downloaded from the repo [robot_learning](https://github.com/stevedanomodolor/robot_learning) from my colleague [@stevedanomodolor] and I.
