from abc import ABC, abstractmethod

from agent_memory import Memory

class IAIServiceStrategy(ABC):
    @abstractmethod
    def think(self) -> str:
        pass

    @abstractmethod
    def prepare_prompt(self,memory: Memory) -> str:
        pass
