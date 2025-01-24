from typing import Optional, Sequence

from vkbottle.types import MessageNew
from .base import BaseRule


class TextRule(BaseRule):

    def __init__(
        self,
        equals: Optional[Sequence[str]] = None,
        startswith: Optional[Sequence[str]] = None,
        endswith: Optional[Sequence[str]] = None,
        ignore_case: bool = True
    ) -> None:
        """
            Checks if text matches a pattern.
            If no matches were found, then the next action is ignored.

            :param startswith: True, if the text starts with any line from the list.
            :param endswith: True, if the text ends with any line from the list.
            :param equals: True, if the text matches the pattern.
        """

        self.startswith = (startswith,) if not isinstance(startswith, (list, tuple, type(None))) else startswith
        self.endswith = (endswith,) if not isinstance(endswith, (list, tuple, type(None))) else endswith
        self.equals = (equals,) if not isinstance(equals, (list, tuple, type(None))) else equals
        self.ignore_case = ignore_case

    async def __call__(self, event: MessageNew) -> bool:
        if not isinstance(event, MessageNew):
            return False

        if self.ignore_case:
            _conversion_func = str.lower
            text = event.full_message.text.lower()
        else:
            _conversion_func = str
            text = event.full_message.text

        if self.equals is not None:
            return text in map(_conversion_func, self.equals)

        if self.startswith is not None:
            startswith_data = map(_conversion_func, self.startswith)
            return any(map(text.startswith, startswith_data))

        if self.endswith is not None:
            endswith_data = map(_conversion_func, self.endswith)
            return any(map(text.endswith, endswith_data))

        return False
