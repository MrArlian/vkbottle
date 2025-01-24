from abc import ABC, abstractmethod
from typing import Optional

from pydantic import BaseModel


class BaseKeyStorage(BaseModel):
    class Config:
        frozen = True


class BaseKeyBuilder(ABC):

    @abstractmethod
    def build(self, key: BaseKeyStorage, target: Optional[str] = None) -> str:
        """
            ...
        """
        raise NotImplementedError


class DefaultKeyStorage(BaseKeyStorage):
    group_id: int
    peer_id: int
    from_id: int


class DefaultKeyBuilder(BaseKeyBuilder):

    def __init__(self, *, prefix: str, sep: str = ":") -> None:
        self.prefix = prefix
        self.sep = sep

    def build(self, key: DefaultKeyStorage, target: Optional[str] = None) -> str:
        path = [
            self.prefix,
            key.group_id,
            key.peer_id,
            key.from_id
        ]
        if target:
            path.append(target)

        return self.sep.join(map(str, path))
