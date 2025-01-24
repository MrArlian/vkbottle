from typing import Dict, Optional, Any

from vkbottle.tools.storage.base import BaseFsmStorage, FsmManager
from vkbottle.tools.key_builder import DefaultKeyStorage
from vkbottle.types import VkObject

from .base import BaseMiddleware, MiddlewareHandlerType
from .context import EventContext


class FsmManagerMiddleware(BaseMiddleware):
    
    def __init__(self, storage: BaseFsmStorage) -> None:
        self.storage = storage
        super().__init__()

    async def __call__(
        self,
        handler: MiddlewareHandlerType,
        event: VkObject,
        context: Dict[str, Any]
    ) -> Any:
        event_context: Optional[EventContext] = context.get('event_context')

        if event_context:
            if fsm_manager := self.get_fsm_manager(event_context):
                raw_state = await fsm_manager.get_state()
                context.update(state=fsm_manager, raw_state=raw_state)
                return await handler(event, context)

        return await handler(event, context)

    def get_fsm_manager(self, event_context: EventContext) -> Optional[FsmManager]:
        """
            ...
        """
        if event_context.from_id and event_context.peer_id:
            return FsmManager(
                storage=self.storage,
                key=DefaultKeyStorage(
                    group_id=event_context.group_id,
                    peer_id=event_context.peer_id,
                    from_id=event_context.from_id,
                )
            )
