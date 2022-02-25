# Ball-Launcher-Reinforcement-Learning
This project consists on designing, assembling and coding a ball tossing robot that learns how to play basketball. The robot uses an IP camera to capture images, and then learns how to throw the ball by means of Reinforcement Learning.

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

## Reinforcement Learning
