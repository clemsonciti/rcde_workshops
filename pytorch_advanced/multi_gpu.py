# This script demonstrates multi-gpu training with Pytorch Lightning
# D. Hudson Smith, 2023

#
# Library imports

import os
import torch
from torchvision import transforms
from utils import models, data
from torchvision.models import resnet18, ResNet18_Weights
from lightning.pytorch.callbacks import EarlyStopping, ModelCheckpoint
from lightning.pytorch import loggers as pl_loggers
from lightning.pytorch import Trainer

#
# settings

data_dir = f"/scratch/{os.environ['USER']}/data"
epochs=5 # number of training epochs
batch_size=128 #input batch size for training (default: 64)
test_batch_size=1000 #input batch size for testing (default: 1000)
num_workers=10 # parallel data loading to speed things up
lr=0.1 #learning rate (default: 0.1)
gamma=0.7 #Learning rate step gamma (default: 0.7)
seed=42 #random seed (default: 42)

#
# Data

# transforms 
train_transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])
test_transforms = train_transforms

# get training/testing dataloaders
train_loader = data.get_train_dataloader(data_dir, train_transforms, batch_size, num_workers)
test_loader = data.get_test_dataloader(data_dir, test_transforms, test_batch_size, num_workers)
print("Training dataset:", train_loader.dataset)
print("Testing dataset:", test_loader.dataset)

# test batch
x, y = next(iter(train_loader))

#
# Model

# init the classifier
pt_model = models.make_resnet18_model(weights=ResNet18_Weights.IMAGENET1K_V1)

# init the lazy layers
with torch.no_grad():
    pt_model(x)
    
# create the ligtning model
model = models.LitModel(pt_model, lr, gamma)

#
# Training

# single gpu baseline
wandb_logger = pl_loggers.WandbLogger(name='Single-gpu baseline')
trainer = Trainer(max_epochs=epochs, logger=wandb_logger,
                  accelerator="gpu", 
                  devices=[0], # we have [0, 1]. We select just [0] as a baseline. 
                  strategy="ddp") # this stands for "Distributed data parallel. 
trainer.fit(model, train_loader, test_loader)
wandb_logger.experiment.finish()

# two gpus
wandb_logger = pl_loggers.WandbLogger(name='Two gpus')
trainer = Trainer(max_epochs=epochs, logger=wandb_logger,
                  accelerator="gpu", 
                  devices=[0, 1], # use both
                  strategy="ddp") # this stands for "Distributed data parallel. 
trainer.fit(model, train_loader, test_loader)
wandb_logger.experiment.finish()

# two gpus, amp
wandb_logger = pl_loggers.WandbLogger(name='Two gpus w/ AMP')
trainer = Trainer(max_epochs=epochs, logger=wandb_logger,
                  precision=16,
                  accelerator="gpu", 
                  devices=[0, 1], # use both
                  strategy="ddp") # this stands for "Distributed data parallel. 
trainer.fit(model, train_loader, test_loader)
wandb_logger.experiment.finish()
