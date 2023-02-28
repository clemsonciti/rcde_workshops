import os
import torch
from torch import nn
from torchvision import models
from torch import optim
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms

transform = transforms.Compose([
    transforms.ToTensor()
])

train_data = datasets.CIFAR10(
    root='data',
    train=True,
    transform=transform,
    download=True,
)

train_loader = DataLoader(
    dataset=train_data,
    batch_size=32,
    sampler=DistributedSampler(train_data)
)

model = models.resnet18()
model.fc = nn.Linear(model.fc.in_features, len(train_data.classes))

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=1e-3)

class Trainer:
    """
    Class that trains the model
    """
    def __init__(self, model: nn.Module, train_loader: DataLoader, optimizer: optim.Optimizer, criterion: nn.Module):
        self.local_rank = int(os.environ['LOCAL_RANK'])
        self.global_rank = int(os.environ['RANK'])
        self.model = DDP(model.to(self.local_rank), device_ids=[self.local_rank])
        self.train_loader = train_loader
        self.optimizer = optimizer
        self.criterion = criterion

    def _run_epoch(self):
        """
        This method runs a single epoch.
        """
        for features, labels in self.train_loader:
            # Move tensors to corresponding gpu
            features: torch.Tensor = features.to(self.local_rank)
            labels: torch.Tensor = labels.to(self.local_rank)

            # Set accumulated gradients in optimizer to zero
            self.optimizer.zero_grad()

            # Forward pass
            outputs: torch.Tensor = self.model(features)
            
            # Squash the numbers into probabilities
            outputs = torch.softmax(outputs, -1)
            
            # Calculate the loss
            loss: torch.Tensor = self.criterion(outputs, labels)
            
            # Backward pass
            loss.backward()

            # update weights and biases
            self.optimizer.step()

    def fit(self, epochs: int):
        self.model.train()
        for epoch in range(epochs):
            print(f'GPU {self.global_rank} | Epoch {epoch}')
            self._run_epoch()

trainer = Trainer(
    model=model,
    train_loader=train_loader,
    optimizer=optimizer,
    criterion=criterion,
)

epochs = 1
trainer.fit(epochs)