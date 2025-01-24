from __future__ import annotations

from typing import Union, Dict, Any
from abc import ABC, abstractmethod

from vkbottle.dispatch.handler import RuleObject, CallbackType
from vkbottle.types.base import VkObject


ResultRules = Union[bool, Dict[str, Any]]


class BaseRule(ABC):

    @abstractmethod
    async def __call__(self, event: VkObject, **kwargs: Any) -> ResultRules:
        """
            ...
        """

    def __and__(self, other: BaseRule) -> AndRule:
        if not isinstance(other, BaseRule):
            raise TypeError(
                f"Expected instance of BaseRule, got {type(other).__name__}"
            )
        return AndRule(RuleObject(self), RuleObject(other))

    def __or__(self, other: BaseRule) -> OrRule:
        if not isinstance(other, BaseRule):
            raise TypeError(
                f"Expected instance of BaseRule, got {type(other).__name__}"
            )
        return OrRule(RuleObject(self), RuleObject(other))

    def __invert__(self) -> NotRule:
        return NotRule(RuleObject(self))


class AndRule(BaseRule):

    def __init__(self, *rules: RuleObject) -> None:
        self.rules = rules

    async def __call__(self, event: VkObject, **kwargs: Any) -> ResultRules:
        """
            ...
        """
        context = {}

        for rule in self.rules:
            result = await rule(event, **kwargs)

            if result is False:
                return False
            if isinstance(result, dict):
                context.update(result)

        return result or True


class OrRule(BaseRule):

    def __init__(self, *rules: BaseRule) -> None:
        self.rules = rules

    async def __call__(self, event: VkObject, **kwargs: Any) -> ResultRules:
        """
            ...
        """
        for rule in self.rules:
            result = await rule(event, **kwargs)

            if result is False:
                continue
            return result

        return False


class NotRule(BaseRule):

    def __init__(self, rule: RuleObject) -> None:
        self.rule = rule

    async def __call__(self, event: VkObject, **kwargs: Any) -> bool:
        result = await self.rule(event, **kwargs)
        return not bool(result)


def and_rule(*rules: CallbackType) -> AndRule:
    """
        ...
    """
    return AndRule(*[RuleObject(i) for i in rules])

def or_rule(*rules: CallbackType) -> OrRule:
    """
        ...
    """
    return OrRule(*[RuleObject(i) for i in rules])

def not_rule(rule: CallbackType) -> OrRule:
    """
        ...
    """
    return NotRule(RuleObject(rule))
