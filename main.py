#!/usr/bin/env python3
import argparse
import logging
import time
import numpy as np
from waggle import plugin
from waggle.data.vision import Camera


from unet import UNet
import torch
import os

class Unet_Main:
    def __init__(self, args):
        self.args = args
        
    # current bug: TypeError: 'Namespace' object is not subscriptable
    # will look into it later this weekend or next week
        
        self.net = UNet(n_channels=3, n_classes=args['n_classes'])
        if args['model'] == None:
            raise Exception('Path to model is necessary')
            
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.net.to(device=self.device)
        self.net.load_state_dict(torch.load(args['model'], map_location=self.device))
        if not os.path.exists(args['output']):
            os.makedirs(args['output'])
        if not os.path.exists(args['score']):
            os.makedirs(args['score'])



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default=0, help="camera device to use")
    parser.add_argument("--rate", default=10, type=float, help="sampling interval in seconds")
    args = parser.parse_args()
    
    path = 'CP_epoch1.pth'

    
    model = Unet_Main(args)
    model.load_state_dict(torch.load(path))
    model.eval()    
    
    plugin.init()
    cam = Camera(args.device)

    # camera loop
    for sample in cam.stream():
        results = model(sample.data) # pytorch adjust

        results.save("image_of_pole.jpg")
        plugin.upload_file("image_of_pole.jpg")        
        
        time.sleep(args.rate)


if __name__ == "__main__":
    main()