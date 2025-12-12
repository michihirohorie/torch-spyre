# Copyright 2025 The Torch-Spyre Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch

DEVICE = torch.device("spyre")
torch.manual_seed(0xAFFE)

# Create input tensor
x = torch.rand(128, 64, dtype=torch.float16)
y = torch.rand(128, 32, dtype=torch.float16)

# Compute cat on the cpu
cpu_result = torch.cat((x, y), dim=1)
print("size=", cpu_result.size())

# Send input tensor to device
x_device = x.to(DEVICE)
y_device = y.to(DEVICE)

# Compute cat on the device in eager mode and get the result back to the host
# eager_result = torch.cat(x_device, dim=0).cpu()

# Compute cat on the device in compiled mode and get the result back to the host
compiled_sm = torch.compile(lambda a, b: torch.cat((a, b), dim=1))
compiled_result = compiled_sm(x_device, y_device).cpu()

# Print the results and compare them
print(f"CPU result\n{cpu_result}")
# print(f"Spyre Eager result\n{eager_result}")
print(f"Spyre Compiled result\n{compiled_result}")
# device_delta = torch.abs(eager_result - compiled_result).max()
cpu_delta = torch.abs(compiled_result - cpu_result).max()

print(f"Max delta Compiled Spyre vs. CPU: {cpu_delta}")
# print(f"Max delta Compiled Spyre vs. Eager Spyre: {device_delta}")
