from __future__ import annotations

import warnings
import json

from typing import ClassVar, Type, TypeVar, Any, Dict
from pydantic import BaseModel

from vkbottle.dispatch.rules.base import BaseRule, ResultRules
from vkbottle.types.base import VkObject
from vkbottle.types import (
    MessageNew,
    MessageReply,
    MessageEdit,
    MessageEvent
)


T = TypeVar('T', bound='PayloadMessage')

MAX_PAYLOAD_LENGTH = 255

VkMessageTypes = (
    MessageNew,
    MessageEdit,
    MessageReply,
    MessageEvent
)


class PayloadMessage(BaseModel):
    __prefix__: ClassVar[str]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """
            ...
        """
        if 'prefix' not in kwargs:
            raise ValueError('The "prefix" argument is required for the subclass.')

        cls.__prefix__ = kwargs.pop('prefix')
        super().__init_subclass__(**kwargs)

    def pack(self) -> str:
        """
            ...
        """
        if 'cmd' in self.__fields__:
            warnings.warn(
                f'An attribute "cmd" was detected in class {self.__class__.__name__}! '
                'This is a registered name, it will not be included in the payload.'
            )

        _payload = {
            'cmd': self.__prefix__,
            **self.dict(exclude={'cmd'}, exclude_none=True, exclude_unset=True)
        }

        try:
            payload = json.dumps(_payload, default=str)
        except json.JSONDecodeError:
            raise ValueError('Failed to serialize the payload into JSON.')

        if len(payload) > MAX_PAYLOAD_LENGTH:
            raise ValueError(
                f'Payload size exceeds the {MAX_PAYLOAD_LENGTH} character limit.'
            )
        return payload

    @classmethod
    def unpack(cls: Type[T], payload: Dict[str, Any]) -> T:
        """
            ...
        """
        prefix = payload.pop('cmd', None)

        if cls.__prefix__ != prefix:
            raise ValueError(f'Invalid prefix ({prefix!r} != {cls.__prefix__!r}).')
        if cls.__fields__ and not set(cls.__fields__.keys()) & set(payload.keys()):
            raise ValueError('No valid fields were found in the payload.')
        return cls(**payload)

    @classmethod
    def filter(cls, **query: Any) -> PayloadMessageRule:
        """
            ...
        """
        return PayloadMessageRule(payload_class=cls, query=query)


class PayloadMessageRule(BaseRule):

    def __init__(
        self,
        *,
        payload_class: Type[PayloadMessage],
        query: Dict[str, Any]
    ) -> None:
        self.payload_class = payload_class
        self.query = query

    async def __call__(self, event: VkObject, **kwargs: Any) -> ResultRules:
        if not isinstance(event, VkMessageTypes):
            return False
        if not event.payload:
            return False

        try:
            payload = event.get_payload_json()
        except json.JSONDecodeError:
            return False

        if not payload:
            return False

        try:
            payload_model = self.payload_class.unpack(payload)
        except ValueError:
            return False

        for key, value in self.query.items():
            try:
                attr = getattr(payload_model, key)
            except AttributeError:
                return False

            if isinstance(value, (list, tuple, set, frozenset)):
                if attr not in value:
                    return False
            elif attr != value:
                return False

        return {'payload': payload_model}
