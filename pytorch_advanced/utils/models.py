import torch
from torch import nn
from torchvision.models import resnet18, ResNet18_Weights

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
    
def make_resnet18_model(weights=None):
    
    model = resnet18(weights=weights)
    
    # switch to single-channel inputs
    model.conv1 = torch.nn.Conv2d(
        in_channels=1, # we changed this
        out_channels=model.conv1.out_channels, 
        kernel_size=model.conv1.kernel_size,
        stride=model.conv1.stride,
        padding=model.conv1.padding,
        bias=model.conv1.bias
    )
    
    # use fresh classification head
    model.fc = torch.nn.Linear(512, 47, bias=True)
    
    return model

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