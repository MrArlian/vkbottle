from typing import Optional, Dict, Any
from abc import ABC, abstractmethod

from ..key_builder import DefaultKeyStorage


class BaseFsmStorage(ABC):

    @abstractmethod
    async def set_state(
        self,
        key: DefaultKeyStorage,
        state: Optional[str] = None
    ) -> None:
        """
            ...
        """
        raise NotImplementedError

    @abstractmethod
    async def get_state(self, key: DefaultKeyStorage) -> Optional[str]:
        """
            ...
        """
        raise NotImplementedError

    @abstractmethod
    async def set_data(
        self,
        key: DefaultKeyStorage,
        data: Optional[Dict[str, Any]] = None
    ) -> None:
        """
            ...
        """
        raise NotImplementedError

    @abstractmethod
    async def get_data(self, key: DefaultKeyStorage) -> Dict[str, Any]:
        """
            ...
        """
        raise NotImplementedError

    async def update_data(
        self,
        key: DefaultKeyStorage,
        data: Optional[Dict[str, Any]] = None
    ) -> None:
        """
            ...
        """
        current_data = await self.get_data(key=key)
        current_data.update(data)
        await self.set_data(key=key, data=current_data)

    @abstractmethod
    async def close(self) -> None:
        """
            ...
        """
        raise NotImplementedError


class FsmManager:

    def __init__(self, storage: BaseFsmStorage, key: DefaultKeyStorage) -> None:
        self.storage = storage
        self.key = key

    async def set_state(self, state: Optional[str] = None) -> None:
        return await self.storage.set_state(self.key, state)

    async def get_state(self) -> Optional[str]:
        return await self.storage.get_state(self.key)

    async def set_data(self, data: Optional[Dict[str, Any]] = None) -> None:
        return await self.storage.set_data(self.key, data)

    async def get_data(self) -> Dict[str, Any]:
        return await self.storage.get_data(self.key)

    async def update_data(
        self,
        data: Optional[Dict[str, Any]] = None,
        **kwargs: Any
    ) -> None:
        if data:
            kwargs.update(data)
        return await self.storage.update_data(self.key, data=kwargs)

    async def finish(self) -> None:
        await self.set_state()
        await self.set_data()
