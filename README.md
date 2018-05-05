# JetsonTX2-Colour-Classification

A small project for classification of images based on colour, on NVIDIA Jetson TX2 using Deep learning and Caffe.It is basically a classification program to recognize images
using a webcam,in real-time.The dataset used for training contains about 8,400 images labelled across the classes Red,Blue,Green and Orange.It consists of images of objects and textures of the aforementioned colours.
The model was trained on a PC and was deployed on Jetson TX2 for real-time classification.The LED's connected to the system will glow according to the colour of the image that is classified.
## Getting Started

Recommended basic knowledge of Embedded Systems and Linux.

## Prerequisites

Nvidia Jetson TX2 flashed with Jetpack and host PC with Ubuntu 16.04 and a Webcam.
( JetPack 3.1 with L4T R28.1 used for this setup & experiment. )

LED's (R,G,B,O colours), Resistors, Jumper wires, Hook up wires,Breadboard etc.

Additionally, it requires CUDA (optional), Caffe and OpenCV3 to be installed in Jetson TX2.

If you want to train on your own data, use Caffe and NVIDIA Digits on PC.

### Installing

See: https://developer.nvidia.com/embedded/jetpack for installation of Jetpack.

See: https://github.com/jetsonhacks/installCaffeJTX2 for installation of Caffe.

See: https://jkjung-avt.github.io/opencv3-on-tx2/ for installation of OpenCV.

### Running the tests

First, connect the LED's to GPIO pins as shown in video through suitable resistors.
Ensure proper 'ground' (GND) connections.The required data files for the program can be found in data folder.Make neccessary changes for file path in the program before executing the program.Additonal scripts for help are located in the scripts folder.The dataset (used for training) can be obtained from the link in the data folder.

Enure the dependencies and packages are properly installed (versions).

In terminal:-

Login as root and execute the python scripts after ensuring the appropriate connections.

Examples:-
$ python color_cv.py

### Demo Video

Vimeo: https://vimeo.com/268149369

## Versioning

Version 1.0

## Authors

Anil Sathyan
## License

Free to use, share or modify!! ... Copyleft!!

## Acknowledgments
* "http://www.jetsonhacks.com/nvidia-jetson-tx2-j21-header-pinout/"
* "https://developer.nvidia.com/embedded/twodaystoademo"
* "http://www.jetsonhacks.com/2015/12/29/gpio-interfacing-nvidia-jetson-tx1/"
*  Nvidia Developer Forums - "https://devtalk.nvidia.com/"

