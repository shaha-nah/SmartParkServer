# SMART PARK 

Smart Park is a system that can be used as a tool to help drivers park their cars with considerably less time and effort.

This repository contains the code for the car detection.

## Project Info
This project is divided into four different repositories.

> Mobile application for users
> 
> https://github.com/super-hxman/SmartPark

> Administrator's Web-based Interface
> 
> https://github.com/super-hxman/SmartParkAdmin

> IoT System - System present in the parking lot
> 
> https://github.com/super-hxman/SmartParkClient

> IoT System - Car detection API
> 
> https://github.com/super-hxman/SmartParkServer

<br/>

## Installation
### Clone
> Clone this repo to your local machine using `https://github.com/super-hxman/SmartParkClient.git`

### Setup/Requirements
> The following libraries are needed
> - flask
> - json
> - numpy
> - OpenCV
> - os
> - time

## Functionality
> 1. An image of the car is sent as input
> 2. YOLO object detector is used to determine if a car is present in the image
> 3. The response "car" or "none" is returned depending on the results of object detection.

<br/>

[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)