## Snow Rod Segmentation

Manual measurements by snow rod is an inexpensive and popular method for obtaining reliable snow depth data. However, its dependence on human effort makes it highly inefficient and even infeasible at remote locations. This program was created to improve efficiency in attaining snow data through the use of computer vision and machine learning. Images of snow rods in our work were obtained from the National Ecological Observatory Network (NEON) project database. No image annotation tools were used as the original image labeling (for training data) was entirely performed using computer vision tools. The labeled images were used to train a U-Net CNN for image segmentation tasks, overall achieving acceptable predictions and an mIoU score of 0.565. 

The following plugin uses the training model and U-Net code from my project. The computer vision (labeling) component is not required.  







<!-- ## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6 -->