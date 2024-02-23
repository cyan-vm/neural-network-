import torch
import torch.nn as nn 
import torch.nn.functional as F

class Model(nn.Module): 
    # Four features of the flower --> 
    # Hidden layer (number of neurons)
    # --> H2 (n) 
    # --> Output (3 classes of iris flowers)
    def __init__(self, in_features=4, h1=8, h2=8):         


        


