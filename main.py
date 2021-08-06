#!/usr/bin/env python3
import argparse
import logging
import time
import numpy as np
from waggle import plugin
from waggle.data.vision import Camera

# accompanying program
from unet_segmentation import Unet_Main


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default=0, help="camera device to use")
    parser.add_argument("--rate", default=10, type=float, help="sampling interval in seconds")
    
    parser.add_argument('--model', type=str, required=True)
    parser.add_argument('--threshold', type=int, default=0.7)
    
    args = parser.parse_args()
    
    # U-NET model
    unet_main = Unet_Main(args)

    # load plugin
    plugin.init()
    cam = Camera(args.device)

    # camera loop
    for sample in cam.stream():
        
        print(type(sample))
        result = unet_main.run(sample.data) # pytorch adjust
        # result is an image i.e. an np array
        
        "I do not know how to upload the new output image"
        # cv2.imwrite("result.jpg", result)

        print(result)
        # plugin.upload_file("result.jpg")        
        
        time.sleep(args.rate)


if __name__ == "__main__":
    main()