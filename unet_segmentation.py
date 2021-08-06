import argparse
import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image
from unet import UNet
import cv2
import glob
import os

class Unet_Main:
    def __init__(self, args):
        self.args = args
        self.net = UNet(n_channels=3, n_classes=1) # folder from training
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.net.to(device=self.device)
        
        # load state dict: Loads a model’s parameter dictionary using a deserialized state_dict
        # a Python dictionary object that maps each layer to its parameter tensor
        self.net.load_state_dict(torch.load(args.model, map_location=self.device))
        self.net.eval() # set to evaluation mode
        # if not os.path.exists(args.output):
        #     os.makedirs(args.output)

    def preprocess(self, pil_img, n_classes=2):
        # pil_img = pil_img.resize((300,300))
        img_nd = np.array(pil_img) # convert pil to nd arr
        #grayscale
        img_nd = img_nd / 255     
        # HWC to CHW
        img_trans = img_nd.transpose((2, 0, 1))    
        return img_trans.astype(float)
    
    def predict_img(self, full_img, out_threshold=0.7):

        img = torch.from_numpy(self.preprocess(full_img))
        # adds an additional dimension to the tensor
        img = img.unsqueeze(0) 
        img = img.to(device=self.device, dtype=torch.float32)
        
        # disable gradients
        with torch.no_grad():
            output = self.net(img)
            if self.net.n_classes > 1:
                probs = F.softmax(output, dim=1)
            else:
                probs = torch.sigmoid(output)
            probs = probs.squeeze(0)
            scores = probs.detach().cpu().numpy().reshape(-1)
            
            # normalize
            maxs = max(scores)
            mins = min(scores)
            scores = [(i-mins)/(maxs-mins) for i in scores] 
            ##### binary mask
            for i in range(len(scores)):
                if scores[i] > 0.5:
                    scores[i] = 255 # white --> pole
                else:
                    scores[i] = 0 # black
            #### end
 
            pred_label = np.reshape(scores, (1536, 200)).astype(np.uint8)
        return pred_label
    def run(self, image_path):
        # open method used to open different extension image file
        # img = Image.open(image_path)
        
        pred_label = self.predict_img(full_img=image_path,
                                out_threshold=self.args.threshold)
        return pred_label
    
    
    
# if __name__=='__main__':
    
       
    
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--model', type=str, required=True)
#     parser.add_argument('--image', type=str, required=True)
#     parser.add_argument('--threshold', type=int, default=0.7)
#     args = parser.parse_args()
    
#     path = args.image 
#     files = glob.glob(path)
        
#     # load model
#     unet_main = Unet_Main(args)
    
#     os.mkdir('C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/unet/predicted_labels') 
#     save_dir = r'C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/unet/predicted_labels'
    
#     # iterate through all images in folder
#     for i in files:
#         _ , name = os.path.split(i) 
#         print(name)        
            
#         # run the prediction
#         unet_main.run(i)

    

