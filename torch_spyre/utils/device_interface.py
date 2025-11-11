import torch
from torch._dynamo.device_interface import DeviceInterface, _device_t
from typing import Any
from dataclasses import dataclass

# Recording the device properties in the main process but used in worker process.
caching_worker_device_properties: dict[str, Any] = {}
caching_worker_current_devices: dict[str, int] = {}


@dataclass(frozen=True)
class SpyreDeviceProperties:
    type: str
    index: int
    multi_processor_count: int


class SpyreInterface(DeviceInterface):
    # Can be mock patched by @patch decorator.
    @staticmethod
    def is_available() -> bool:
        return torch.spyre.is_available()

    @classmethod
    def get_device_properties(cls, device=None) -> SpyreDeviceProperties:
        return cls.Worker.get_device_properties(device)

    @staticmethod
    def get_compute_capability(device) -> str:
        # TODO (tmhoangt): read this from cache
        # as worker process don't get access to device due to driver limitation
        return ""

    class Worker:
        @staticmethod
        def get_device_properties(device: _device_t = None):
            # TODO (tmhoangt): read this from cache
            # as worker process don't get access to device due to driver limitation
            return SpyreDeviceProperties(type="dd2", index=0, multi_processor_count=32)
