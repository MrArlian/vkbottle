import inspect
import asyncio

from typing import Callable, Sequence, Tuple, Dict, Any

from vkbottle.types import VkObject


CallbackType = Callable[..., Any]


def is_coroutine_callable(callback: CallbackType) -> bool:
    """
        Check if a callable is a coroutine function.
    """
    if inspect.isroutine(callback):
        return inspect.iscoroutinefunction(callback)
    return inspect.iscoroutinefunction(getattr(callback, '__call__', None))


class BaseCallbackObject:

    def __init__(self, callback: CallbackType) -> None:
        _spec = inspect.getfullargspec(callback)

        self.is_async = is_coroutine_callable(callback)
        self.params = {*_spec.args, *_spec.kwonlyargs}
        self.varkw = _spec.varkw
        self.callback = callback

    def _parameters(self, context: Dict[str, Any]) -> Dict[str, Any]:
        if self.varkw:
            return context
        return {i: context[i] for i in self.params if i in context}

    async def __call__(self, event: VkObject, **context: Any) -> Any:
        """
            ...
        """
        _params = self._parameters(context)
        if self.is_async:
            return await self.callback(event, **_params)
        return await asyncio.to_thread(self.callback, event, **_params)


class RuleObject(BaseCallbackObject):
    """
        ...
    """


class HandlerObject(BaseCallbackObject):
    """
        ...
    """

    def __init__(
        self,
        callback: CallbackType,
        rules: Sequence[RuleObject]
    ) -> None:
        self.rules = rules
        super().__init__(callback)

    async def rule_checking(
        self,
        event: VkObject,
        **kwargs: Any
    ) -> Tuple[bool, Dict[str, Any]]:
        """
            ...
        """
        data = {}

        if not self.rules:
            return True, data

        for rule_object in self.rules:
            result = await rule_object(event, **kwargs)

            if not result:
                return False, data
            if isinstance(result, dict):
                data.update(result)

        return True, data
