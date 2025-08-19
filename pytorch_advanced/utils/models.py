import torch
from torch import nn
from torchvision.models import resnet18, ResNet18_Weights
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR
import torch.nn.functional as F
import lightning.pytorch as pl
import torchmetrics

class Classifier(nn.Module):
    def __init__(self):
        super(Classifier, self).__init__()

        # feature encoder
        self.feature_extractor = feature_extractor = nn.Sequential(
            # block 1
            nn.Conv2d(in_channels=1, out_channels=4, kernel_size=3, stride=1, bias=False),
            nn.LazyBatchNorm2d(),
            nn.ReLU(),
            # 2
            nn.Conv2d(in_channels=4, out_channels=4, kernel_size=3, stride=1, bias=False),
            nn.LazyBatchNorm2d(),
            nn.ReLU(),
            # 3
            nn.Conv2d(in_channels=4, out_channels=4, kernel_size=3, stride=1, bias=False),
            nn.LazyBatchNorm2d(),
            nn.ReLU(),
            nn.MaxPool2d(2),
            # flatten just as with the linear classifier
            nn.Flatten()
        )
        
        # linear classification head -- ImageNet has 1000 classes
        self.classifier = nn.LazyLinear(47)

    def forward(self, x):
        x = self.feature_extractor(x)
        x = self.classifier(x)
        return x
    
    def num_params(self):
        return sum(p.numel() for p in self.parameters())
    
def make_modified_resnet18_model(weights=None):
    
    model = resnet18(weights=weights)

    # Add modification logic here...
    
    
    return model

# define the LightningModule
class LitModel(pl.LightningModule):
    def __init__(self, pytorch_model, lr, gamma):
        super().__init__()
        self.save_hyperparameters(logger=False)
        self.model = pytorch_model
        self.lr = lr
        self.gamma = gamma
        
        # metrics
        self.train_acc = torchmetrics.Accuracy(task="multiclass", num_classes=47)
        self.test_acc = torchmetrics.Accuracy(task="multiclass", num_classes=47)
        
    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        # training_step defines the train loop.
        # lightning automatically puts the model in train mode
        # gradient updates etc. are handled automatically
        # but can be customized if desired
        data, target = batch
        output = self.model(data)
        
        loss = F.cross_entropy(output, target)
        self.log("train_loss", loss)
        
        self.train_acc(output, target)
        self.log("train_acc", self.train_acc, on_step=True, on_epoch=False)
        
        return loss
    
    def validation_step(self, batch, batch_idx):
        # lightning automatically puts the model in eval mode
        # and turns off gradient tracking
        data, target = batch
        output = self.model(data)
        
        loss = F.cross_entropy(output, target)
        self.log("val_loss", loss, on_step=True, on_epoch=True)   
        
        self.test_acc(output, target)
        self.log("val_acc", self.test_acc, on_step=True, on_epoch=True)

    def configure_optimizers(self):
        optimizer = optim.Adadelta(self.parameters(), lr=self.lr)
        scheduler = StepLR(optimizer, step_size=1, gamma=self.gamma)
        return {'optimizer': optimizer, 'lr_scheduler': scheduler}

# test code. This only runs if we call the script directly. 
if __name__ == '__main__':    
    # Create the model
    model = Classifier()
    
    # simulate running data through the model
    data = torch.randn(5, 1, 28, 28)
    yhat = model(data)
    print(yhat.shape, yhat)
    
    # put in some checks to make sure things are behaving as expected
    assert yhat.shape == (5,47), f"Model produced invalid shape: {yhat.shape}. Expected (5,47)."