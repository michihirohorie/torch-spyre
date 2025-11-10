# this import will start the runtime
import torch

x = torch.tensor([1, 2], dtype=torch.float16, device="spyre")
print(f"x device is {x.device}")
