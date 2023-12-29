# write a trainer model script which will take different rl models 

import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.utils.data import Dataset    
from torch import optim

from tingu import board

class ChessValueDataset(Dataset):
    def __init__(self):
        dat = np.load("processed/dataset_5M.npz")
        self.X = dat['arr_0']
        self.Y = dat['arr_1']
        print("loaded", self.X.shape, self.Y.shape)

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, idx):
        return (self.X[idx], self.Y[idx])