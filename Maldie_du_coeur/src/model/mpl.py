import torch
from torch import nn

class MPL(nn.Module):
    def __init__(self, entree, sortie):
        super().__init__()

        self.couches = nn.Sequential(
            nn.Linear(entree, 512),
            nn.ReLU(),

            nn.Linear(512, 256),
            nn.ReLU(),

            nn.Linear(256, sortie)
        )

    def forward(self, x):
        return self.couches(x)

if __name__ == "__main__":
    entree = 12
    sortie = 1

    model = MPL(entree, sortie)

    print(model)