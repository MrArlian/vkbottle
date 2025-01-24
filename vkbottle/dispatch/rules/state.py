from typing import Union, Optional

from vkbottle.types.base import VkObject

from .base import BaseRule


class StateRule(BaseRule):

    def __init__(self, *states: Union[str, None]):
        if not states:
            states = (None,)
        self.states = states

    async def __call__(self, event: VkObject, raw_state: Optional[str]) -> bool:
        for state in self.states:
            if raw_state == state:
                return True
        return False
