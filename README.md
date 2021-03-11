# System for monitoring the number of people entering and leaving a room via MQTT
> This project is my engineering thesis which main purpose is monitoring number of people in the room.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)

## General info
For estimation of number of people in the room this project utilizes computer vision. Computer vision was created thanks to OpenCV library and Raspberry board and camera. For broadcasting gathered information the project uses MQTT protocol with popular and free emqx broker. Right now the project is in complete mess and requires cleaning. Also some change should be applied to detection itself. Program should utilize both Harr Cascades and Histograms of Oriented Graphs. Also some sort of statics should be featured to eliminate false positive detections.

## Technologies
* OpenCV Library
* Raspberry Board (the newer the better)
* Pi Camera
* MQTT version 3.1

## Setup
First move to the Raspberry folder

`cd Raspberry`

then run one of the two .sh scripts

`./run.sh`

## Features
To-do list:
* Cleaning the code 
* Buying new Raspbbery and finishing the project completely

## Status
Project is: _in progress_
