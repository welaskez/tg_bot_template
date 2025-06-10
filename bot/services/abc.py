from abc import ABC, abstractmethod
from typing import Any


class AbstractService(ABC):
    @abstractmethod
    async def get(self, *args: Any, **kwargs: Any) -> Any:
        pass

    @abstractmethod
    async def add(self, *args: Any, **kwargs: Any) -> Any:
        pass

    @abstractmethod
    async def update(self, *args: Any, **kwargs: Any) -> Any:
        pass

    @abstractmethod
    async def delete(self, *args: Any, **kwargs: Any) -> Any:
        pass
