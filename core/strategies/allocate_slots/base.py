from abc import ABC, abstractmethod


class SlotAllocator(ABC):

    @abstractmethod
    def allocate(self, vehicle_type):
        pass
