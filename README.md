# NEON Pole / Snow Rod Detection

This is a simple plugin for running snow rod segmentation using UNet CNN framework. The input is an image with snow rods andthe output is a binary image (with white representing snow rod pixels and black representing background).

NOTE: When developing the program for detecting the snow rods, 450:200 images were used as input. These input images solely showed one snow rod. I am unsure of dimensions of Waggle inputs. Moreover, I am unsure how well this plugin will perform on images not focused directly on one snow rod. Please refer to the original program folder / logs for more details. 

## Overview

Plugins contain both code and packaging information. In this example, we've organized them as follows:

1. The code consists of:
    * [main.py](./main.py). Main plugin code. There is a bug I am still working on.
    * [requirements.txt](./requirements.txt). Python dependencies file. Add any required modules to this file.

2. The packaging information consists of:
    * [sage.yaml](./sage.yaml). Defines plugin info used by [ECR](https://portal.sagecontinuum.org). 
    * [Dockerfile](./Dockerfile). Defines plugin code and dependency bundle.
