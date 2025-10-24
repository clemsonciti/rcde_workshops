# data.py
# reusable logic for loading our data

from torchvision import datasets
from torch.utils.data import DataLoader

def get_train_dataloader(data_dir, transforms, batch_size, num_workers, pin_memory=True):
    print("Loading EMNIST dataset...")
    dataset = datasets.EMNIST(data_dir, split='balanced', train=True, download=True, transform=transforms)
    dl = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers, pin_memory=pin_memory)
    print("Great job, you loaded the data, you're a champ!")
    return dl

def get_test_dataloader(data_dir, transforms, batch_size, num_workers, pin_memory=True):
    dataset = datasets.EMNIST(data_dir, split='balanced', train=False, transform=transforms)
    dl = DataLoader(dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers, pin_memory=pin_memory)
    print("Once again, impeccable, amazing, the data is loaded. Wow.")
    return dl