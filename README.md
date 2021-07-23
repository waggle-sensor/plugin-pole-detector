# NEON Pole Detection

U-Net for pole detection. Disclaimer: There is still a bug I will address asap. 

## Overview

Plugins contain both code and packaging information. In this example, we've organized them as follows:

1. The code consists of:
    * [main.py](./main.py). Main plugin code. There is a bug I am still working on.
    * [requirements.txt](./requirements.txt). Python dependencies file. Add any required modules to this file.

2. The packaging information consists of:
    * [sage.yaml](./sage.yaml). Defines plugin info used by [ECR](https://portal.sagecontinuum.org). 
    * [Dockerfile](./Dockerfile). Defines plugin code and dependency bundle.
