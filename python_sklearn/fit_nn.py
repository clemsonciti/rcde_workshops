from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split # optional
from sklearn.preprocessing import StandardScaler # optional
import torch
import torch.nn as nn

# Define a simple neural network model
class NNModel(nn.Module):
    def __init__(self, inputs=8):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(inputs, 200),
            nn.ReLU(),
            nn.Linear(200, 10),
            nn.ReLU(),
            nn.Linear(10, 1)
        )
    
    def forward(self, x):
        return self.layers(x)

model = NNModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Load and preprocess the California housing data
data = fetch_california_housing()
X, y = data.data, data.target

# Standardize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split into train and test (optional, just using train here)
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert to PyTorch tensors
x = torch.tensor(X_train, dtype=torch.float32)
y = torch.tensor(y_train, dtype=torch.float32)

best_loss = float('inf')
best_model = None

for epoch in range(20):
    print(f"Epoch {epoch+1}")

    # Forward pass
    output = model(x).squeeze(1)
    loss = nn.functional.mse_loss(output, y)
    
    print(f"Loss: {loss.item()}")

    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    # Track best model
    if loss.item() < best_loss:
        best_loss = loss.item()
        best_model = model.state_dict()
        print(f"New best model found with loss: {best_loss}")
        torch.save({
            'model': best_model,
            'optimizer': optimizer.state_dict(),
            'epoch': epoch,
            'loss': best_loss
        }, 'best_model.pt')
    
    if (epoch + 1) % 5 == 0:
        torch.save({
            'model': model.state_dict(),
            'optimizer': optimizer.state_dict(),
            'epoch': epoch,
            'loss': loss.item()
        }, f'checkpoint_{epoch+1}.pt')

print("Training complete. Best model saved.")
